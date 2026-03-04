from django.contrib import admin
from .models import ProductCategory, Manufacter, Product, Cart, CartsElement

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Manufacter)
class ManufacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category', 'manufacter')
    search_fields = ('name', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(CartsElement)
class CartsElementAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
# Register your models here.
