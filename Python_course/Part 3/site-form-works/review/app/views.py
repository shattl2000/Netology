from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponseRedirect, get_object_or_404

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get(self.pk_url_kwarg, None))

    def get_context_data(self, **kwargs):
        current_product = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        context['reviews'] = Review.objects.filter(product=current_product)
        if self.request.session.get('has_commented_product', False):
            context['has_commented_obj'] = self.request.session.get('has_commented_product')
            if self.kwargs.get(self.pk_url_kwarg, None) in self.request.session.get('has_commented_product', []):
                context['is_review_exist'] = True
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        form = ReviewForm(self.request.POST)
        has_commented_product = self.request.session.get('has_commented_product', [])
        if form.is_valid() and pk not in has_commented_product:
            review = form.save(commit=False)
            review.product_id = pk
            review.save()
            has_commented_product.append(pk)
            self.request.session['has_commented_product'] = has_commented_product
        return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))
