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


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # New field
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)  #  new field
    opening_hours = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    def __str__(self):
        return self.name
