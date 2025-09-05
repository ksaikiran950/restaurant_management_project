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
    image=models.ImageField(upload_to='restaurant_images/'blank=True,null=True)
    opening_hours = models.JSONField(default=dict, blank=True)
    logo = models.ImageField(upload_to="restaurant_logos/",blank=True,null=True)

    def __str__(self):
        return self.name


class TodaySpecial(models.py):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name =models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.sub,itted_at.strftime('%Y-%m-%d %H:%M')}"
