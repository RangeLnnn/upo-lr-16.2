from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('author/',views.aboutauthor),
    path('about/',views.aboutshop),
    path('',views.mainpage),
    path('catalog/',views.catalog),
    path('catalog/<int:pk>/',views.produkt_detail),
    path('cart/',views.cart),
    path('registrate/',views.registrate),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('cart/add/<int:product_id>',views.add_product),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    


]