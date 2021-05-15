from django.contrib import sitemaps
from django.urls import reverse

# Products related
from product.models import Product
from product.urls import urlpatterns as productUrls

# News related
from news.models import News
from news.urls import urlpatterns as newsUrls

# About us
# from IE104_SC.urls import urlpatterns as mainUrls

class StaticSitemap(sitemaps.Sitemap):
    changefreq = 'never'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['recommend', 'about']
    
    def location(self, item):
        return reverse(item)


class ProductSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

class NewsSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
    
    def location(self, obj):
        return obj.get_absolute_url()