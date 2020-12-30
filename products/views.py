from django.shortcuts import render, get_object_or_404
from products.models import Coffee
# Create your views here.


def products(request):
    coffees = Coffee.objects.all()
    data = {
        'co_site': coffees,
    }
    return render(request, 'products/products.html', data)

def coffee_detail(request, id):
    single_coffee = get_object_or_404(Coffee, pk=id)
    data = {
        'single_coffee': single_coffee,
    }
    return render(request, 'products/coffee_detail.html', data)




