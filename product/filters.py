from django.utils.functional import empty
import django_filters
from .models import Product, SKINTYPE_CHOICE, SKINCOND_CHOICE
from multiselectfield import MultiSelectField


"""Create a filter for product in the recommend section"""


class ProductFilter(django_filters.FilterSet):
    skinCondition = django_filters.filters.ChoiceFilter(
        label='Skin Condition', field_name='skinCondition', lookup_expr='icontains', empty_label='No Special Condition', choices=SKINCOND_CHOICE)
    skinType = django_filters.filters.ChoiceFilter(
        label='Skin Type', field_name='skinType', lookup_expr='icontains', empty_label='All Skin Type', choices=SKINTYPE_CHOICE)

    class Meta:
        model = Product
        fields = {
            'skinCondition',
            'skinType',
        }

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()