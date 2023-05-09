

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_page, contact_page
from client.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('sobre/', about_page, name='about_page'),
    path('contato/', contact_page),
    path('cliente/', include('client.urls')),
    path('produto/', include('product.urls')),
    path('login/', login_page, name='login_page')
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
