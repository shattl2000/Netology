from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from customer.models import Product, Order, ProductCustomerCart, ProductCustomer, Customer
from shop.views import add_menu_data


class CustomerFormView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        self.object = form.save()
        Customer.objects.create(user=self.object)
        return super(CustomerFormView, self).form_valid(form)


def get_customer(request):
    customer = None
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        customer = user.customer.first()
    return customer


@login_required
def show_user_profile(request):
    total_price = None
    customer = get_customer(request)
    cart = customer.cart.all()
    if cart:
        total_price = 0
        for item in cart:
            total_price += item.sum_price()
    context = {'customer': customer,
               'cart': cart,
               'total_price': total_price}
    context = add_menu_data(context)
    return render(request,
                  'user_profile.html',
                  context=context)


@login_required
def add_to_cart(request, id):
    if request.user.is_authenticated:
        customer = get_customer(request)
        product = Product.objects.get(id=id)
        item, created = ProductCustomerCart. \
            objects.get_or_create(product=product,
                                  customer=customer,
                                  defaults={'qty': 1})
        if not created:
            item.qty = item.qty + 1
            item.save()
    return redirect('/')


@login_required
def make_order(request):
    customer = get_customer(request)
    cart = customer.cart.all()
    order = Order.objects.create(customer=customer)
    for item in cart:
        ProductCustomer.objects.create(product=item.product,
                                       order=order,
                                       qty=item.qty)
    customer.products_in_cart.clear()
    for item in cart:
        item.delete()
    return redirect('/accounts/profile/')
