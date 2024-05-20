from django.urls import path
from .views import home, offer


urlpatterns = [
    path("home/", home),
    
]