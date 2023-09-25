# added by Maya
# this will create separate views for regular users and companies + render different templates based on user types

from django.shortcuts import render
from .models import User

def regular_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'regular_user_profile.html', {'user': user})

def company_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'company_profile.html', {'user': user})