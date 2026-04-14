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
    prosucts = Product.objects.all()
    return render(request,'catalog.html',{'products':prosucts})
def produkt_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'productdetail.html',{'product':product})
def cart(request):
    cart = Cart.objects.filter(user_id=request.user.id).first()
    if cart:
        items = CartsElement.objects.filter(cart_id=cart.id)
    return render(request,'cart.html',{'items':items})
# Create your views here.
