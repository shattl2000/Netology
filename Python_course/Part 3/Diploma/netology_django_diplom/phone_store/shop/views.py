from collections import OrderedDict
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from urllib.parse import urlencode
from articles.models import Article
from shop.models import Product, Category


def add_menu_data(context):
    categories = Category.objects.filter(parent=None).order_by('name')
    category_tree = OrderedDict()
    for category in categories:
        category_tree[category.name] = []
        for section in category.childs.all():
            sections = category_tree[category.name]
            sections.append((section.name, section.slug))
            category_tree[category.name] = sections
    context['category_tree'] = category_tree
    return context

def show_index(request):
    articles = Article.objects.all()
    products = Product.objects.order_by('?')[:3]
    context = {'articles': articles,
               'products': products}
    context = add_menu_data(context)
    return render(request,
                  'index.html',
                  context=context)


def show_product(request, category, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    context = add_menu_data(context)
    return render(request,
                  'phone.html',
                  context=context)


def get_products_rows(products, columns):
    iter_counter = len(products) // columns
    last_less_row = len(products) % columns
    products_rows = []
    for i in range(iter_counter):
        products_rows.append(products[i:i+columns])
    if last_less_row:
        start_slice = iter_counter * columns
        products_rows.append(products[start_slice:start_slice + last_less_row])
    return products_rows


def show_category(request, category):
    category_object = Category.objects.get(slug=category)
    all_products = category_object.products.all()
    columns = 3
    rows = 1
    products_rows = get_products_rows(all_products, columns)
    paginator = Paginator(products_rows, rows)
    current_page = request.GET.get('page')
    if not current_page:
        current_page = 1
    current_page = int(current_page)
    url_begin = reverse('show_category', args=(category,))
    products_page = paginator.page(current_page)
    next_page_url = None
    prev_page_url = None
    if paginator.num_pages > current_page:
        next_page = current_page + 1
        next_page_url = f'{url_begin}?{urlencode({"page": next_page})}'
    if current_page >= 2:
        prev_page = current_page - 1
        prev_page_url = f'{url_begin}?{urlencode({"page": prev_page})}'
    context = {'products_page': products_page,
               'category': category_object,
               'current_page': current_page,
               'next_page_url': next_page_url,
               'prev_page_url': prev_page_url}
    context = add_menu_data(context)
    return render(request, 'category.html', context=context)
