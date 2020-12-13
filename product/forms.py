from django import forms
from .models import Product

class Recommend(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'