import django_filters
<<<<<<< HEAD
from .models import Product

class ProductFilter (django_filters.FilterSet):
    class Meta:
        model = Product
        fields =  ['skintype','skin_cond']
=======

from .models import Product

"""Create a filter for product in the recommend section"""
class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = [
            'skin_cond', 'skintype'
        ]
>>>>>>> d784b27e8124ccc2361736b21f6f0ffccab1524d
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()