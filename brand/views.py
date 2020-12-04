from django.shortcuts import render

from django.views import generic

from .models import Brand
from product.models import Product

# Create your views here.
"""Print brand list"""
class BrandList(generic.ListView):
    model = Brand
    template_name = 'brand/base_brandList.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        brands = Brand.objects.all()
        return brands
        """ brandsNameArr = []
        for brand in brands:
            name = brand.get_branding_name_display()
            brandsNameArr.append(name)
        return brandsNameArr """
        
        
"""Print all product in xxx brand """
def BrandPList(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    products = Product.objects.all()
    productSelected = []
    for product in products:
        if product.brand_id == brand_id:
            productSelected.append(product)

    context = {
        'products': productSelected, 
    }
    return render(request, 'brand/base_brandPList.html', context)