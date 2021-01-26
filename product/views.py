from django.shortcuts import render
from django.views import View
from .models import Product


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        count = Product.objects.count()
        return render(request, 'product/product.html', {'products': products, 'count': count})
