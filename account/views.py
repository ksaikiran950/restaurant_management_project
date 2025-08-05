# views.py
import requests
from django.shortcuts import render

def home(request):
        try:
            response = requests.get('http://localhost:8000/menu-items/')  # Replace with your actual API endpoint
            menu_items = response.json()
        except:
            menu_items = []

        return render(request, 'home.html', {'menu_items': menu_items})
