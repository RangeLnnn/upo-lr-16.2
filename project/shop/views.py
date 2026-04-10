from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def aboutauthor(request):
    return render(request,'aboutauthor.html')
def aboutshop(request):
    return render(request,'aboutshop.html')
def mainpage(request):
    return render(request,'mainpage.html')
def catalog(request):
    return render(request,'catalog.html')
def produkt_detail(request,pk):
    product = Product.objects.get(pk=pk)
    if product.quantity > 0:
        stock_status = f"✅ В наличии: {product.quantity} шт."
    else:
        stock_status = "❌ Нет в наличии"


    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{product.name}</title>
    </head>
    <body>
        <h1>{product.name}</h1>
        
        <table border="1" cellpadding="10">
            <tr><th>Характеристика</th><th>Значение</th></tr>
            <tr><td>Категория</td><td>{product.category.name}</td></tr>
            <tr><td>Производитель</td><td>{product.manufacter.name} ({product.manufacter.country})</td></tr>
            <tr><td>Описание</td><td>{product.description}</td></tr>
            <tr><td>Цена</td><td>{product.price} руб.</td></tr>
            <tr><td>Наличие</td><td>{stock_status}</td></tr>
        </table>
        
        <h3>О производителе</h3>
        <p>{product.manufacter.description}</p>
        
        <h3>О категории</h3>
        <p>{product.category.description}</p>
        
        <hr>
        <p>
            <a href="/shop/catalog/">В каталог</a> | 
            <a href="/shop/">На главную</a>
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)
# Create your views here.
