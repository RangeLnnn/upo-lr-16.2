from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_receipt
from rest_framework import viewsets
from .seriralizers import *
from django.core.paginator import Paginator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


def aboutauthor(request):
    return render(request,'aboutauthor.html')
def aboutshop(request):
    return render(request,'aboutshop.html')
def mainpage(request):
    return render(request,'mainpage.html')
#def catalog(request):
    #products = Product.objects.all()
    #return render(request,'catalog.html',{'products':products})
def produkt_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'newproductdetail.html',{'product':product})
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
@login_required
def checkout(request):
    if request.method == 'POST':
        subject=request.user.username
        message=f"Спасибо за покупку {request.user.username}"
        from_email=settings.EMAIL_HOST_USER
        to_email=request.POST.get('email')
        email=EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[to_email],
        )
        cart = Cart.objects.filter(user_id=request.user.id).first()
        if cart:
            items = CartsElement.objects.filter(cart_id=cart.id)
        else:
            items = []  
        general_price=cart.general_price() 
        excel_file=generate_receipt(user=request.user,items=items,total_price=general_price)
        email.attach("receipt.xlsx", excel_file.read(), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        email.send()
        return redirect('/shop/cart/')
    else:
        cart = Cart.objects.filter(user_id=request.user.id).first()
        if cart:
            items = CartsElement.objects.filter(cart_id=cart.id)
        else:
            items = []  
        general_price=cart.general_price() 
        return render(request,'checkout.html',{'items':items,'general_price':general_price})
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        
        category = self.request.query_params.get('category')
        manufacturer = self.request.query_params.get('manufacturer')
        search = self.request.query_params.get('search')

        if category:
            queryset = queryset.filter(category_id=category)
            
        if manufacturer:
            queryset = queryset.filter(manufacter_id=manufacturer)
            
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset
class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
class ManufacterViewSet(viewsets.ModelViewSet):
    queryset = Manufacter.objects.all()
    serializer_class = ManufacterSerializer
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    @action(detail=False, methods=['post'], url_path='add')
    def add_to_cart(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({'error': 'product_id required'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем, авторизован ли пользователь (для API)
        if not request.user.is_authenticated:
            return Response({'error': 'Пользователь не авторизован'}, status=status.HTTP_401_UNAUTHORIZED)

        # Получаем товар
        product = get_object_or_404(Product, pk=product_id)
        
        # Находим или создаем корзину для текущего юзера
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Находим или создаем элемент в корзине
        cart_item, item_created = CartsElement.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'success': True, 'message': 'Товар добавлен в корзину'}, status=status.HTTP_200_OK)
class CartsElementViewSet(viewsets.ModelViewSet):
    queryset=CartsElement.objects.all()
    serializer_class=CartsElementSerializer
def index(request):
    popular_products=Product.objects.all().order_by('-id')[:6]
    categories=ProductCategory.objects.all()
    return render(request,'index.html',{'popular_products':popular_products,'categories':categories})
def maincatalog(request):
    products = Product.objects.all()
    paginator = Paginator(products,9)
    page_number=request.GET.get('page')
    pageobj = paginator.get_page(page_number)
    categories = ProductCategory.objects.all()
    manufacters=Manufacter.objects.all()
    return render(request,'newcatalog.html',{ 'products': pageobj,'categories': categories,'manufacturers': manufacters,})










# Create your views here.
