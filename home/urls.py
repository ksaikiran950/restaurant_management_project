from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact_us,name='contact_us')
    path('', views.homepage, name='homepage'),
    path('reservations/', views.reservations, name='reservations'),
    
]