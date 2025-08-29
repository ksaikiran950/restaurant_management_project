from django.shortcuts import render

# Create your views here.
def place_order(request):
    return render(request,'orders/place_order.html')


def order_confirmation(request):
    order_number = random.randint(100000,999999)
    return render(request,'order/order_confirmation.html',{'order_number':order_number})



def view_cart(request):
    cart = request.session.get('cart',[])
    total = sum(item['price'] for item in cart)
    return render(request,'orders/cart.html',{'cart':cart,'total':total})