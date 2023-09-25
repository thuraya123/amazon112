from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from .models import CustomUser  # Import the CustomUser model

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle user registration logic here
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page after registration
        else:
            # Check for password validation errors
            if 'password1' in form.errors:
                messages.error(request, 'Password is not valid. Please choose a stronger password.')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect based on the user's category
            if user.is_customer:  # Check if the user is a regular customer
                return redirect('reg_user_profile', username=user.username)
            elif user.is_organization:  # Check if the user is an organization/company
                return redirect('company_user_profile', username=user.username)
        else:
            # Display an error message for invalid login credentials
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
