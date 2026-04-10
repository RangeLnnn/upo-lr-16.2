from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('author/',views.aboutauthor),
    path('about/',views.aboutshop),
    path('',views.mainpage),
    path('catalog/',views.catalog),
    path('catalog/<int:pk>/',views.produkt_detail),

]