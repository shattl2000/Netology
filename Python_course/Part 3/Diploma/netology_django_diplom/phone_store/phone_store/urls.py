"""phone_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.views as auth_views
from django.urls import path
from shop.views import show_index, show_product, show_category
from customer.views import show_user_profile, add_to_cart, make_order,\
                           CustomerFormView
from articles.views import show_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('register/', CustomerFormView.as_view()),
    path('accounts/profile/', show_user_profile),
    path('', show_index, name='index'),
    path('articles/<slug:slug>/', show_article),
    path('category/<str:category>/', show_category, name='show_category'),
    path('category/<str:category>/<int:id>/', show_product, name='show_product'),
    path('add-to-cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('accounts/profile/make-order', make_order, name='make_order')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
