from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import FormClient



def client_page(request):
    template_name = 'client\index.html'
    form = FormClient(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login\index.html')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, template_name, context)    

def login_page(request):
    context = {
        "title": "Pagina login",
        "content": "Sejam Bem Vindos !! "
    }
    return render(request, "login\index.html", context)    

# def client_page(request):
#     form = FormClient()
   
#     return render(request, "client\index.html", {'form': form })  
