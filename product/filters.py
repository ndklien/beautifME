import django_filters

from .models import Product

"""Create a filter for product in the recommend section"""
class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = [
            'skin_cond', 'skintype'
        ]