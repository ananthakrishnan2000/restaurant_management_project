from django.conf import settings
from django.shortcuts import render

def menu_items(request):
    items = [
        {"name": "Fish Nirvana", "price": "$5"},
        {"name": "Chicken Biriyani", "price": "$8"},
        {"name": "Porota", "price": "$2"},
        {"name": "Tea", "price": "$1"}
    ]
    
    return render(request, "menu.html" , {"items": items})
