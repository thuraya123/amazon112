# created by Maya
# creating the two User models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Common fields for both regular users and companies
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    pickup_location = models.CharField(max_length=120, blank=True, null=True)
    
    # Additional fields for regular users
    is_company = models.BooleanField(default=False)
    
    # Additional fields for companies
    company_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)