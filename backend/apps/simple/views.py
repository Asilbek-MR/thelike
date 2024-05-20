from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,  "index.html")



def registr(request):
    return render(request, 'register.html')



def login(request):
    return render(request, 'login.html')


def offer(request):
    return render(request,'offer.html')