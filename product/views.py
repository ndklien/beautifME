from django.shortcuts import render

from django.views import generic

#simple search ussing q
from django.db.models import Q

from . import views
from .models import Product

# Create your views here.
def Homepage(request):
    return render(request, 'product/base.html')

"""Search toolbar"""
class SearchResults(generic.ListView):
    model = Product
    template_name = 'product/base_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(description__icontains=query)
        )


""" Print all products """
class ProductListView(generic.ListView):
    model = Product
    template_name = 'product/base_productList.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()

""" Print product details """
def productDetail(request, question_id):
    product = Product.objects.get(pk=question_id)
    context = {
        'product': product,
    }

    return render(request, 'product/base_productDetail.html', context)

""" Print all brands """
class BrandListView(generic.ListView):
    model = Product
    template_name = 'product/base_brandList.html'
    context_object_name = 'brands_list'

    def get_queryset(self):
        products = Product.objects.all()
        brandList = []
        for p in products:
            name = p.get_branding_name_display()
            if name not in brandList:
                brandList.append(name)
            else:
                pass
        return brandList


"""Print all product in xxx brand """
class PbrandListView(generic.ListView):
    model = Product
    template_name = 'product/base_brandDetail.html'
    context_object_name = 'brandproducts_list'

    def get_queryset(self):
        pass