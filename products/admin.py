from django.contrib import admin
from .models import Product


class PriceInlineAdmin(admin.TabularInline):
    model = Product
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Product, ProductAdmin)