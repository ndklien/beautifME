from django.contrib import sitemaps
from django.urls import reverse

from product.models import Product
from news.models import News

class ProductSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Product.objects.all()

class NewsSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return News.objects.all()