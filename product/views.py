from django.shortcuts import render

#local import
from . import views
from .models import Product

#class-based views
from django.views import generic

#search engine
from django.db.models import Q

# Create your views here.
def Homepage(request):
    return render(request, 'product/base.html')

class SearchRequest(generic.ListView):
    model = Product
    template_name = 'product/base_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Q(
            Q(product_name__icontains=query) |
            Q(description__icontains=query)
        )