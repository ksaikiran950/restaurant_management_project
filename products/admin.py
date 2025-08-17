from django.contrib import admin
from .models import *

from django.contrib import adminfrom .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'price', 'is_available', 'created_at']
    list_filter = ['restaurant', 'is_available']
    search_fields= ['name', 'description']



class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)