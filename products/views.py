from django.shortcuts import render, get_object_or_404
from .models import Coffee
# Create your views here.


def products(request):
    coffees = Coffee.objects.all()
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            coffees = coffees.filter(Product_Name__icontains=name)
    if 'searchdesc' in request.GET:
        name = request.GET['searchdesc']
        if name:
            coffees = coffees.filter(description__icontains=dec)
    data = {
        'Products': coffees,
    }
    return render(request, 'products/products.html', data)

def product(request, id):
    single_coffee = get_object_or_404(Coffee, pk=id)
    data = {
        'single_coffee': single_coffee,
 }
    return render(request, 'products/product.html', data)

def search(request):
    return render(request, 'products/search.html')





