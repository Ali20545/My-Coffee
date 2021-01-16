from django.shortcuts import render
from products.models import Coffee
# Create your views here.

def home(request):
    l_coffee = Coffee.objects.order_by('-create_date')
    data = {
        'latest_coffee': l_coffee,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')


def coffee(request):
    return render(request, 'pages/coffee.html')



