from django.contrib import admin
from django.contrib.auth.models import User
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    filter_horizontal = ['products']

    # def get_phones(self, obj):
    #     phones = obj.phones.all()
    #     str_phones = '/n'.join(phone.model for phone in phones)
    #     return str_phones
    # get_phones.short_description = 'Телефоны'


admin.site.register(Article, ArticleAdmin)
