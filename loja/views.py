from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context ={
        "title": "Pagina Principal",
        "content": "Bem Vindo" 
    }
    return render(request, "index.html", context)

def about_page(request):
    context = {
        "title": "Pagina Sobre ",
        "content": " Bem Vindo a Pagina Sobre !! "
    }
    return render(request, "about\index.html", context)

def contact_page(request):
    context = {
        "title": "Pagina Contato",
        "content": "Bem vindo a Pagina Contato !! "
    }
    return render(request, "contact\index.html", context)
