from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *


class Products(View):
    template_name = 'product/product.html'

    def get(self, request):
        products = Product.objects.all()
        count = Product.objects.count()
        return render(request, self.template_name, {'products': products, 'count': count})


class ProductsDetails(View):
    template_name = 'product/product-details.html'

    def get(self, request, id):
        products = Product.objects.get(pk=id)
        images = Images.objects.filter(product_id=id)
        return render(request, self.template_name, {'products': products, 'images': images})
