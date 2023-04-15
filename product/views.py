from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_page(request):
    products = Product.objects.all()[0:6]
  
    return render (request, "product\index.html",  {'products':products})
