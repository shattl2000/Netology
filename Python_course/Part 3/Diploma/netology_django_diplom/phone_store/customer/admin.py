from django.contrib import admin
from customer.models import Customer, Order


class ProductsInline(admin.StackedInline):
    model = Order.products.through
    fields = ['qty', 'product']


class CustomerOrderInline(admin.StackedInline):
    model = Order


class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerOrderInline]


class OrderAdmin(admin.ModelAdmin):
    def get_products_count(self, obj):
        counter = 0
        for product in obj.orders.all():
            counter += product.qty
        return counter


    sortable_by = 'date'
    inlines = [ProductsInline]
    list_display = ['__str__', 'customer', 'date', 'get_products_count']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
