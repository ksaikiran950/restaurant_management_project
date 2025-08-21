from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"




class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

# Opening hours stored as a JSON object
    opening_hours = models.JSONField(default=dict, blank=True)
    logo = models.ImageField(upload_to="restaurant_logos/",blank=True,null=True)

    def __str__(self):
        return self.name
