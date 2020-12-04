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
        return brands
        """ brandsNameArr = []
        for brand in brands:
            name = brand.get_branding_name_display()
            brandsNameArr.append(name)
        return brandsNameArr """

def BrandPList(request, brand_id):
    brandSelected = Brand.objects.get(pk=brand_id)
    context = {
        'brand': brandSelected, 
    }
    return render(request, 'brand/base_brandPList.html', context)
        