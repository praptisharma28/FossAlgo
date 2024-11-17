from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

def homepage_view(request):
    return render(request,'homepage.html')