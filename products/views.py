from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category, Product
# Create your views here.


def index(req):
    CATEGORIES = Category.objects.all()
    return render(req, 'products/index.html', {'categories': CATEGORIES})


def category(req, category_id):

    products = Product.objects.filter(category=category_id)
    return render(req, 'products/products.html', {'products': products})


def product(req, product_id):
    product = Product.objects.get(id=product_id)
    return render(req, 'products/details.html', {'product': product})
