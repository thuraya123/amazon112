# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    category_choices = (
        ('customer', 'Customer'),
        ('organization', 'Organization'),
    )
    
    category = forms.ChoiceField(
        choices=category_choices,
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'category-radio'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'category')

# views.py
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle user registration logic here
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
        else:
            # Handle form validation errors here
            pass
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})
