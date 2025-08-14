from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
       "restaurant_name": "The Windsor Castle",
       "welcome_message": "Welcome to our restaurant! Enjoy your dining experience."
    }
    
    return render(request, "home.html" , context)
