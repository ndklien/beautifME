import django_filters
from .models import Product

class ProductFilter (django_filters.FilterSet):
    class Meta:
        model = Product
        fields =  ['skintype','skin_cond']
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()