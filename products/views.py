from sre_parse import CATEGORIES
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

CATEGORIES = [
    "smartphones",
    "laptops",
    "fragrances",
    "skincare",
    "groceries",
    "home-decoration",
    "furniture",
    "tops",
    "womens-dresses",
    "womens-shoes",
    "mens-shirts",
    "mens-shoes",
    "mens-watches",
    "womens-watches",
    "womens-bags",
    "womens-jewellery",
    "sunglasses",
    "automotive",
    "motorcycle",
    "lighting"
]


def index(req):
    return render(req, 'products/index.html', {'categories': CATEGORIES})


def category(req, category):

    if category not in CATEGORIES:
        return Http404()
    else:
        return HttpResponse(category)


def product(req):
    return HttpResponse("Product Page")
