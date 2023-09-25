from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('profile1/', views.company_profile, name='company_user'),
    path('profile2/', views.regular_user_profile, name='regular_user'),
    # Add other URL patterns as needed
]
