from django.contrib import admin
from .models import Product, Comment

# Django Summernote configuration
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
