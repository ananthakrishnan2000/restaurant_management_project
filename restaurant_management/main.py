from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

settings.configure(
    DEBUG=True,
    SECRET_KEY='abc123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    RESTAURANT_NAME="My Awesome Restaurant",

)

def home(request):
    return HttpResponse(f"<h1>Welcome to {settings.RESTAURANT_NAME} </h1>")
urlpatterns = [
    path('', home),

]

application = get_wsgi_application()