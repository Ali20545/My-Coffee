from django.shortcuts import render
from .models import Coffee
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def coffee(request):
    return render(request, 'pages/coffee.html')

def signin(request):
    return render(request, 'pages/signin.html')

def signup(request):
    return render(request, 'pages/signup.html')

def profile(request):
    return render(request, 'pages/profile.html')

def search(request):
    return render(request, 'pages/search.html')
