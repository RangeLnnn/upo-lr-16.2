from django.contrib import admin
from .models import ProductCategory, Manufacter, Product, Cart, CartsElement, Profile,Order,OrderItem

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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'full_name', 'phone')
    list_filter = ('role',)
    search_fields = ('user__username', 'full_name', 'phone')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]
# Register your models here.
