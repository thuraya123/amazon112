from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from .models import CustomUser  # Import the CustomUser model

from django.contrib.auth import login, get_backends  # Import get_backends

from django.contrib.auth import login, get_backends
from django.contrib.auth.backends import ModelBackend  # Import the ModelBackend

from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Set the category based on the form input
            category = form.cleaned_data.get('category')
            user.category = category
            user.save()
            
            # Handle user registration logic here
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
        else:
            # Check for password validation errors
            if 'password1' in form.errors:
                messages.error(request, 'Password is not valid. Please choose a stronger password.')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})





from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from .models import CustomUser

from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            category = user.category  # Access the category field
            if category == 'customer':
                return redirect('regular_user_profile', username=user.username)
            elif category == 'organization':
                return redirect('company_profile', username=user.username)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def home(request):
    # Your view logic here
    return render(request, 'home.html')

def regular_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'reg_user_profile.html', {'user': user})

def company_profile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'company_user_profile.html', {'user': user})
