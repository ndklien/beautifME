from django.shortcuts import render

from django.views import generic

#simple search ussing q
from django.db.models import Q

from . import views
from .models import Product

# Create your views here.
def Homepage(request):
    return render(request, 'product/base.html')

class SearchResults(generic.ListView):
    model = Product
    template_name = 'product/base_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(description__icontains=query)
        )

