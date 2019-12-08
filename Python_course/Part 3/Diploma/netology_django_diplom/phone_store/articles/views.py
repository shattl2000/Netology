from django.shortcuts import render
from articles.models import Article
from shop.views import add_menu_data


def show_article(request, slug):
    article = Article.objects.prefetch_related('products').get(slug=slug)
    products = article.products.all()
    context = {'article': article,
               'products': products}
    context = add_menu_data(context)
    return render(request,
                  'article.html',
                  context=context)
