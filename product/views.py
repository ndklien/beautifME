from django.shortcuts import render

from django.views import generic

#simple search ussing q
from django.db.models import Q

from . import views
from .models import Product, Comment
from brand.models import Brand
from django.contrib.auth.models import User
<<<<<<< HEAD
from .forms import Recommend
from .filters import ProductFilter
=======

from .filters import ProductFilter 

>>>>>>> d784b27e8124ccc2361736b21f6f0ffccab1524d
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

<<<<<<< HEAD

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
<<<<<<< HEAD
        'product': product, #"""Sản phẩm"""
        'comments': comment #"""Bình luận của sản phẩm đó"""
    }
    return render(request, 'product/base_productDetail.html', context)

# recommend product

def Recommend(request):
    if request.method == 'GET':
        cleanser = Product.objects.filter(category="CLEANSE")
        remover = Product.objects.filter(category="MAKEUP_RM")
        moist = Product.objects.filter(category="MOIST")
        sun = Product.objects.filter(category="SUN")

        cleanserFilter = ProductFilter(request.GET, queryset=cleanser)
        removerFilter = ProductFilter(request.GET, queryset=remover)
        moistFilter = ProductFilter(request.GET, queryset=moist)
        sunFilter = ProductFilter(request.GET, queryset=sun) 

        cleanserArr = Recommend_result(cleanserFilter)
                
        removerArr = Recommend_result(removerFilter)
                
        moistArr = Recommend_result(moistFilter)

        sunArr = Recommend_result(sunFilter)
                
        context = {
            'filterForm': cleanserFilter,
            'cleanserArr': cleanserArr,
            'removerArr': removerArr,
            'moistArr': moistArr,
            'sunArr': sunArr,
            
            }
    
    return render(request, 'product/base_recommend.html', context)

# Hiển thị ba sản phẩm trong recommend
def Recommend_result(result):
    arr = []
    count = 0
    for c in result.qs:
        if count < 3 :
            arr.append(c)
            count +=1
        else:
            break
    return arr



=======
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

>>>>>>> d784b27e8124ccc2361736b21f6f0ffccab1524d
=======
def Recommendation(request):
    return render(request, 'product/base_recommend.html')


>>>>>>> 0743bd1d190116e291a5cf00f24a6f918ada0ac8
