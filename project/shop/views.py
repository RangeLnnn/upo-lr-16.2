from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
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
    return render(request,'cart.html',{'items':items})
def registrate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registrate.html',{'form': form})







# Create your views here.
