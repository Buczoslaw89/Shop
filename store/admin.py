from django.contrib import admin

# Register your models here.

from . models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_tag', 'category', 'price', 'date_added', 'digital', 'is_feature')
    list_editable = ('name', 'price', 'category', 'is_feature')
admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email')
admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer', 'product', 'date_order', 'complete', 'status')
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
admin.site.register(OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'zipcode', 'date_added')
admin.site.register(ShippingAddress, ShippingAddressAdmin)