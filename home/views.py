from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from products.models import MenuItem

# Optional Restaurant import
try:
    from products.models import Restaurant
except ImportError:
    Restaurant = None


def about(request):
    return render(request, 'home/about.html')


def homepage(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    return render(request, "home/index.html", {"menu_items": menu_items, "query": query})


def reservations(request):
    context = {
        "restaurant_name": "Delicious Bites",
        "restaurant_phone": "+91-9876543210",
    }
    return render(request, "home/reservations.html", context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("contact_success")  # redirect to a success page
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})
}

from .models import Restaurant
def home(request):
    restaurant = Restaurant.objects.first()  # assume one restaurant

    # Get cart info from session
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values()) if cart else 0

    context = {
        "restaurant": restaurant,
        "cart_cot, "home/home.html", context)
}