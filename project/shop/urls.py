from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'product',views.ProductViewSet)
router.register(r'productcategory',views.ProductCategoryViewSet)
router.register(r'manufacter',views.ManufacterViewSet)
router.register(r'cart',views.CartViewSet)
router.register(r'cartselement',views.CartsElementViewSet)

urlpatterns=[
    path('author/',views.aboutauthor),
    path('about/',views.aboutshop),
    path('',views.mainpage),
    path('catalog/',views.catalog),
    path('catalog/<int:pk>/',views.produkt_detail),
    path('cart/',views.cart),
    path('registrate/',views.registrate),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cart/add/<int:product_id>/',views.add_product),
    path('cart/remove/<int:product_id>/',views.remove_product),
    path('cart/update/<int:product_id>/',views.update_elements_in_cart),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('checkout/',views.checkout),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('home/',views.index)


]