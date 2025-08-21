from django.shortcuts import render,redirect
from django.config import settings
from .forms import ContactForm
from products.models import MenuItem

def about(request):
        return render(request, 'home/about.html')


# Try importing Restaurant model if it exists
try:
    from products.models import Restaurantexcept ImportError:
    Restaurant = None

def homepage(request):
    query = request.GET.get('q')
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
        else:
            menu_items = MenuItem.objects.all()
            return render(request,"home/index.html",{"menu_items": menu_items,"query":query})


def reservations(request):
    context = {
        "restaurant_name": "Delicious Bites",
        "restaurant_phone": "+91-9876543210"
        }
        return render(request, "home/reservations.html", context)
    }




def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('home')  # Redirect after submission
        else:
            form = ContactForm()
        return render(request, 'home/homepage.html', {'form': form})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")  # redirect to a success page
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})