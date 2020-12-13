from django.shortcuts import render

from django.views import generic

#simple search ussing q
from django.db.models import Q

from . import views
from .models import Product, Comment
from brand.models import Brand
from django.contrib.auth.models import User

from .filters import ProductFilter 

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
def productDetail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.all() 
    productComment = []
    for comment in comments:
        if comment.product_id == product_id:
            productComment.append(comment)

    context = {
        'product': product, #Sản phẩm
        'comments': productComment, #Bình luận của sản phẩm đó"""
    }
    return render(request, 'product/base_productDetail.html', context)

"""Recommendation views"""
def recommendList(request):
    moist = Product.objects.filter(category='MOIST')

    moistFilter = ProductFilter(request.GET, queryset=moist)

    context = {
        'moistP': moistFilter,
    }

    return render(request, 'product/base_recommend.html', context)

