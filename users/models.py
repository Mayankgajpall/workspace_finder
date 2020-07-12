from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, null=True, default=None)

    def __str__(self):
        return self.company_name