from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'product_price', 'product_stock', 'product_category', 'modified_date', 'is_available'
    )
    prepopulated_fields = {'product_slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
