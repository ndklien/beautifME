from django.shortcuts import render

# views related
from django.views import generic
from . import views

#simple search ussing q
from django.db.models import Q

# import models
from .models import Product, Comment
from brand.models import Brand
from news.models import News
from django.contrib.auth.models import User

from .filters import ProductFilter

# Create your views here.

""" Define number of objects preview on Home page """
def defineLength(object, number):
    if len(object) < number:
        return len(object)
    else:
        return number

def Homepage(request):
    """ Products """
    products = Product.objects.all()
    selectedProd_1 = []
    selectedProd_2 = []
    for i in range(defineLength(products, 4)):
        selectedProd_1.append(products[i])
    
    for i in range(5, 5 + defineLength(products, 4)):
        selectedProd_2.append(products[i])

    """ News """
    news = News.objects.all()
    selectedNews_1 = []
    selectedNews_2 = []

    for i in range(defineLength(news, 4)):
        selectedNews_1.append(news[i])

    for i in range(5, 5 + defineLength(news, 4)):
        selectedNews_2.append(news[i])

    """ Brand """
    brands = Brand.objects.all()
    selectedBrand_1 = []
    selectedBrand_2 = []
    for i in range(defineLength(brands, 4)):
        selectedBrand_1.append(brands[i])

    for i in range(4, 5 + defineLength(brands, 4)):
        selectedBrand_2.append(brands[i])

    context = {
        'productList1': selectedProd_1,
        'productList2': selectedProd_2,
        'newsList1': selectedNews_1,
        'newsList2': selectedNews_2,
        'brandList1': selectedBrand_1,
        'brandList2': selectedBrand_2,
    }

    return render(request, 'product/base_home.html', context)

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
    paginate_by = 12

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
        'product': product, #"""Sản phẩm"""
        'comments': productComment #"""Bình luận của sản phẩm đó"""
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

""" Hiển thị ba sản phẩm trong recommend """
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
