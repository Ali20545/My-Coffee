from django.shortcuts import render
# Create your views here.


def products(request):
    return render(request, 'pages/products.html')

def product(request):
    return render(request, 'pages/product.html')