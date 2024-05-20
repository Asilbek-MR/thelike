from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("register/", views.registr,name='registr'),
    path("login/", views.login, name='login'),
    path("offer/", views.offer, name='offer'),
]