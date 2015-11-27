from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)


class CartAdmin(admin.ModelAdmin):
    pass


class PurchaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Purchase, PurchaseAdmin)
