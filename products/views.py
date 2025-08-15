from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Item,menu
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_menu(request):
    menu = [
        {"name": "Paneer Butter Masala","description": "Creamy tomato-based curry with paneer cubes","price": 220.00},
        {"name": "Veg Biryani","description": "Fragrant rice cooked with vegetables and spices","price": 180.00},
        {"name": "Masala Dosa","description": "Crispy dosa filled with spiced potato filling","price": 90.00}]
        return Response(menu)

def menu_list(request):
    try:
        menu_items = Menu.objects.all()
        return render(request, 'products/menu_list.html', {'menu_items': menu_items})
    except Exception as e:
        # Log the error (optional, but recommended)
        print(f"Error fetching menu items: {e}")
        # Show a friendly error message
        return HttpResponse("<h2>Sorry! We couldn't load the menu right now.</h2><p>Please try again later.</p>",
status=500
)

