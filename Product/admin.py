from django.contrib import admin

# Register your models here.
from .models import Product


class ProductView(admin.ModelAdmin):
    list_display = [
        'name', 'weight', 'price', 'created_at', 'updated_at'
    ]


admin.site.register(Product, ProductView)
