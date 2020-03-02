from django.urls import path
from user.views import login, register, profile, logout

urlpatterns = [
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    
]