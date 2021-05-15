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
    paginate_by = 12

    def get_queryset(self):
        brands = Brand.objects.order_by("branding_name")
        return brands
        
        
"""Print all product in xxx brand """
def BrandPList(request, brand_id, slug):
    brand = Brand.objects.get(pk=brand_id)
    products = Product.objects.all()
    productSelected = []
    for product in products:
        if product.brand_id == brand_id:
            productSelected.append(product)

    context = {
        'products': productSelected, 
         'brand': brand,
    }
    return render(request, 'brand/base_brandPList.html', context)