from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=225)
    city =models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    Zip_code = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.address},{self.city},{self.state} - {self.zip_code}"