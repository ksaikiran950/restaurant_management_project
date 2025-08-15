from django.shortcuts import render

def about(request):
        return render(request, 'home/about.html')

from django.shortcuts import render
from django.conf import settings

# Try importing Restaurant model if it exists
try:
    from products.models import Restaurantexcept ImportError:
    Restaurant = None

def homepage(request):
    restaurant_name = getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    phone_number = getattr(settings, "RESTAURANT_PHONE", "Not available")

    # If model exists and has at least one restaurant entry, override values
    if Restaurant and Restaurant.objects.exists():
        restaurant = Restaurant.objects.first()
        restaurant_name = restaurant.restaurant_name        
        phone_number = restaurant.phone_number
        context = {
            "restaurant_name": restaurant_name,
            "phone_number": phone_number    
            }
            return render(request, "home/index.html", context)
}

def reservations(request):
    context = {
        "restaurant_name": "Delicious Bites",
        "restaurant_phone": "+91-9876543210"
        }
        return render(request, "home/reservations.html", context)
    }