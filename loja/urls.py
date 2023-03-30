
from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_page, contact_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('sobre/', about_page),
    path('contato/', contact_page),
    path('cliente/', include('client.urls')),
    path('produto/', include('product.urls'))
   
]