from django.shortcuts import render
from .models import Coffee
# Create your views here.


def products(request):
    coffees = Coffee.objects.all()
    data = {
        'co_site': coffees,
    }
    return render(request, 'pages/products.html', data)
