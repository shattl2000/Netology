from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            phone = phones.order_by('name')
        elif sort == 'min_price':
            phone = phones.order_by('price')
        elif sort == 'max_price':
            phone = phones.order_by('-price')
        elif sort == 'release_date':
            phone = phones.order_by('release_date')
    else:
        phone = phones

    return render(
        request,
        'catalog.html',
        context={'phones': phone}
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    return render(
        request,
        'product.html',
        context={'phone': phone}
)