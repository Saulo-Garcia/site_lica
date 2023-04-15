from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_page, name='client'),
    path('', views.login_page, name='login')
]
