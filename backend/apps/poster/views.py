from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"index.html")



def offer(request):
    return render(request,'offer.html')