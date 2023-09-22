from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    
    # Add any additional fields you want for your user model here
    
    def __str__(self):
        return self.username
