from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'quantity', 'is_available', 'created_at')

admin.site.register(Product, ProductAdmin)
