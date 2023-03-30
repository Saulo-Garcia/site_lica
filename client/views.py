from django.shortcuts import render
from django.http import HttpResponse

def client_page(request):
    context = {
        "title": "Pagina Clientes",
        "content": "Sejam Bem Vindos !! "
    }
    return render(request, "client\index.html", context)    
