from django.shortcuts import render, redirect, get_object_or_404

# views related
from django.views import generic
from . import views
from .models import Product

#class-based views
from django.views import generic

#search engine
from django.db.models import Q, query

#simple search ussing q
from django.db.models import Q

# import models
from .models import Product, Comment
from brand.models import Brand
from news.models import News
from django.contrib.auth.models import User

from .forms import pushCommentForms
from .filters import ProductFilter

# Create your views here.

# Home page queries
def Homepage(request):
    """ Products """
    productsLength = len(Product.objects.all())
    products = []
    for p in range(productsLength, productsLength-8, -4):
        products.append(Product.objects.all()[p-4:p])
    """ News """

    news = []
    for n in range(0, 8, 4):
        news.append(News.objects.order_by('-pub_date')[n: n+4])
    """ Brand """
    brands = []
    for b in range(0, 8, 4):
        brands.append(Brand.objects.filter(brandCategory__contains='TREN')[b: b+4])

    context = {
        'productList': products,
        'newsList': news,
        'brandList': brands,
    }

    return render(request, 'product/base_home.html', context)

def navbarQueries(request):
    trendBrand = Brand.objects.filter(brandCategory__contains="TREN")
    highendBrand = Brand.objects.filter(brandCategory__contains="HIGH")
    drugstoreBrand = Brand.objects.filter(brandCategory__contains="DRUG")

    context = {
        'trending': trendBrand,
        'highend': highendBrand,
        'drugstore': drugstoreBrand,
    }
    return render(request, 'product/base.html', context)

# Search toolbar
class SearchResults(generic.ListView):
    model = Product
    template_name = 'product/base_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__branding_name__icontains=query)
        )

""" Print all products """
class ProductListView(generic.ListView):
    model = Product
    template_name = 'product/base_productList.html'
    context_object_name = 'product_list'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.order_by("product_name")

""" Print product details """
def productDetail(request, product_id, slug):
    #get product id
    productD = Product.objects.get(pk=product_id)

    # read all related comment in product
    comments = Comment.objects.all() 
    productComment = []
    for comment in comments:
        if comment.product_id == product_id:
            productComment.append(comment)

    # Add new comment
    commentForm = pushCommentForms()
    message  = ''
    if request.method == 'POST':
        commentForm = pushCommentForms(request.POST, owner_comment=request.user, product=productD)
        if commentForm.is_valid():
            commentForm.save()
            message = 'Push comment succeed.'
            return redirect('product:product-detail', product_id, slug)
        else:
            commentForm = pushCommentForms()
            message = 'Push comment failed.'

    context = {
        'product': productD, 
        'comments': productComment,
        'new_comment': commentForm,
        'message': message,
    }
    return render(request, 'product/base_productDetail.html', context)

# Recommend product
def Recommend(request):
    if request.method == 'GET':
        removerFilter = ProductFilter(request.GET, queryset=Product.objects.filter(category="MAKEUP_RM"))
        cleanserFilter = ProductFilter(request.GET, queryset=Product.objects.filter(category="CLEANSE"))
        lotionFilter = ProductFilter(request.GET, queryset=Product.objects.filter(category="LOTION"))
        moistFilter = ProductFilter(request.GET, queryset=Product.objects.filter(category="MOIST"))
        sunFilter = ProductFilter(request.GET, queryset=Product.objects.filter(category="SUN")) 

        filterForm = ProductFilter(request.GET, queryset=Product.objects.all())

        # cleanserArr = Recommend_result(cleanserFilter)
        # removerArr = Recommend_result(removerFilter)
        # moistArr = Recommend_result(moistFilter)
        # sunArr = Recommend_result(sunFilter)
                
        context = {
            'filterForm': filterForm,
            'removerQ': removerFilter.qs,
            'cleanserQ': cleanserFilter.qs,
            'lotionQ': lotionFilter.qs,
            'moistQ': moistFilter.qs,
            'sunscreenQ': sunFilter.qs,
        }
    
    return render(request, 'product/base_recommend.html', context)


# """ Hiển thị bốn sản phẩm trong recommend """
def Recommend_result(result):
    arr = []
    count = 0
    for c in result.qs:
        if count < 4 :
            arr.append(c)
            count +=1
        else:
            break
    return arr
