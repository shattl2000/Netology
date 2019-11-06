from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    count = Car.review_count
    list_display = ('brand', 'model', count)
    ordering = ['-pk']


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    search_fields = ['car__brand', 'title']
    ordering = ['-pk']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)