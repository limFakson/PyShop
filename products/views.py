from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer, NewProduct

#/products = index
def index(request):
    products = Product.objects.all()
    new = NewProduct.objects.all()
    return render(request, 'index.html', {'products': products, 'new': new}) 


def new(request):
    new = NewProduct.objects.all()
    return render(request, 'newproducts.html', {'new': new})