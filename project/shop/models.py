from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        items=self.cartselement_set.all()
        price=sum(item.product.price*item.quantity for item in items)
        return price

class CartsElement(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.product.name} - {self.product.quantity} шт."
    def elements_price(self):
        return self.product.price*self.quantity

class Profile(models.Model):
    ROLE_CHOICES = [
        ('CUSTOMER', 'Клиент'),
        ('MANAGER', 'Менеджер'),
        ('ADMIN', 'Администратор'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER', verbose_name="Роль")
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="ФИО")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес")

    def __str__(self):
        return f"Профиль: {self.user.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

class Order(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Новый'),
        ('PAID', 'Оплачен'),
        ('DELIVERED', 'Доставлен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW', verbose_name="Статус")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Общая стоимость")

    def __str__(self):
        return f"Заказ №{self.id} — {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена при покупке")

    def __str__(self):
        return f"{self.product.name if self.product else 'Удаленный товар'} ({self.quantity} шт.)"