from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspaces(models.Model):
    name = models.CharField(max_length=225)
    address = models.TextField()
    image = models.ImageField(default="default.jpg", upload_to="media")
    capacity = models.IntegerField()
    city = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(default='Not Available', max_length=50)

    def __str__(self):
        return self.name

class Bookings(models.Model):
    booking_date = models.DateField()
    booked_space = models.ForeignKey(Workspaces, on_delete=models.CASCADE)
    user_booked = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.booking_date)