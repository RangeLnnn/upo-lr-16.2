from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name


class Manufacter(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField()
    description=models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    products_photo=models.ImageField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    quantity=models.IntegerField()
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    manufacter=models.ForeignKey(Manufacter,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Корзина пользователя {self.user.username}"
    def general_price(self):
        pass

class CartsElement(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.product.name} - {self.product.quantity} шт."
    def elements_price(self):
        return self.product.price*self.product.quantity