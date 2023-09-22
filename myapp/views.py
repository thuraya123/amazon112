from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm  # Import the registration and login forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle user registration logic here
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
            if user.category == 'customer':
                return redirect('home')  # Redirect to the customer home page
            elif user.category == 'organization':
                return redirect('home')  # Redirect to the organization home page
        else:
            # Display an error message for invalid login credentials
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    # Your view logic here
    return render(request, 'home.html')
