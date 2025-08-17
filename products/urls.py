from django.urls import path
from . import views

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',views.menu_list,name='menu_list'),
    path('contactc',views_contact_view,name='contact'),
    path('menu/',view.menu_view,name='menu'),

]