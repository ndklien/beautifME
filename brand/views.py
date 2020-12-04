from django.shortcuts import render

from django.views import generic

from .models import Brand
# Create your views here.
class BrandList(generic.ListView):
    model = Brand
    template_name = 'brand/base_brandList.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        brands = Brand.objects.all()
        brandsNameArr = []
        for brand in brands:
            name = brand.get_branding_name_display()
            brandsNameArr.append(name)
        return brandsNameArr

class BrandPList(generic.ListView):
    model = Brand
    template_name = 'brand/base_brandPList.html'
    context_object_name = 'brandp_list'

    def get_queryset(self, brand_id):
        brand = Brand.objects.get(pk=brand_id)
        return brand
        