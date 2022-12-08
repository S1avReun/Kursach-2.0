from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request,
                  'products.html',
                  {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id)
    return render(request,
                  'detail.html',
                  {'product': product})