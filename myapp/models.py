from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Fields common to both regular users and companies
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    pickup_location = models.CharField(max_length=120, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    
    # Fields specific to regular users
    is_customer = models.BooleanField(default=False)
    
    # Fields specific to companies
    is_organization = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    # Add the category field
    category = models.CharField(max_length=20, choices=[('customer', 'Customer'), ('organization', 'Organization')])

    def __str__(self):
        return self.username
