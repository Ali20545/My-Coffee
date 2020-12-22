from django.shortcuts import render
from pages.models import Coffee
# Create your views here.


def products(request):
    coffee = Coffee.objects.all()
    data = {
        'coffee': coffee,
    }
    return render(request, 'pages/products.html', data)

def product(request):
    return render(request, 'pages/product.html')