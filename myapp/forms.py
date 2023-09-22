from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

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
        model = CustomUser  # Use your custom user model
        fields = ('username', 'email', 'password1', 'password2', 'category')

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
