from django.shortcuts import render
from django.http import HttpResponse
def aboutauthor(request):
    return render(request,'aboutauthor.html')
def aboutshop(request):
    return render(request,'aboutshop.html')
def mainpage(request):
    return render(request,'mainpage.html')
# Create your views here.
