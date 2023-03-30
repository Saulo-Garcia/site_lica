from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_page(request):
    context = {
        "title": "Pagina de Produtos",
        "content": "Bem Vindo a Produtos !!"
    }
    return render (request, "product\index.html", context)
