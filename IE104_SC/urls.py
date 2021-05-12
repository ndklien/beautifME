"""IE104_SC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import product.views as productV, news.views as newsV, accounts.views as accountV
import brand.views as Brand

# Media and Ckeditor
from django.conf.urls.static import static
from IE104_SC import settings
import os

from django.contrib.auth import views as authV

from django.contrib.sitemaps.views import sitemap
from sitemaps import ProductSitemap, NewsSitemap, StaticSitemap

# Rich Text Field

# Sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from django.views.decorators.cache import cache_page


sitemaps = {
    'product': ProductSitemap,
    'news': NewsSitemap,
    'static': StaticSitemap,
}


urlpatterns = [
    path('', productV.Homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')), 
    path('news/', include('news.urls')),
    path('brand/', include('brand.urls')),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
    path('logout/', accountV.LogoutView.as_view(), name='logout'),
    path('register/', accountV.registration, name='register'),
    path('login/', authV.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('change_password/',accountV.change_password, name='change_password'),

    # Others
    path('search/', productV.SearchResults.as_view(), name='search_results'),
    path('recommend/', productV.Recommend, name='recommend'),
    path('about/', accountV.aboutView, name='about'),

    # rich text field
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # sitemap
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('site-<section>.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

# if settings.dev.DEBUG:
#     urlpatterns += [re_path('djga/', include('google_analytics.urls')),]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
