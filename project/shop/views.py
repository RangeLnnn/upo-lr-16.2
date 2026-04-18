from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
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
@login_required
def cart(request):
    cart = Cart.objects.filter(user_id=request.user.id).first()
    if cart:
        items = CartsElement.objects.filter(cart_id=cart.id)
    else:
        items = []  
    general_price=cart.general_price()     
    return render(request,'cart.html',{'items':items,'general_price':general_price})
def registrate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registrate.html',{'form': form})
@login_required
def add_product(request,product_id):
    product=Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartsElement.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/shop/catalog/')
@login_required
def remove_product(request,product_id):
    cart_item = CartsElement.objects.get(pk=product_id,cart__user=request.user)
    cart_item.delete()
    return redirect('/shop/cart/')
@login_required
def update_elements_in_cart(request,product_id):
    cart_item=CartsElement.objects.get(pk=product_id)
    new_quntity=request.POST.get('quantity')
    cart_item.quantity=new_quntity
    cart_item.save()
    return redirect('/shop/cart/')
#надо сделать так чтобы при удалении удалялся только один в теории и сделать обновление чтобы обновлялось кол-во

    








# Create your views here.
