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
from django.urls import path, include
import product.views as productV, news.views as newsV, accounts.views as accountV
import brand.views as Brand

from django.contrib.auth import views as authV
urlpatterns = [
    path('', productV.Homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')), 
    path('news/', include('news.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', accountV.registration, name='register'),
    path('login/', accountV.login_user, name='login'),
    path('search/', productV.SearchResults.as_view(), name='search_results'),
    path('brand/', include('brand.urls')),
    path('recommend/', productV.Recommend, name='recommend'),
    path('change_password/',accountV.change_password, name='chang_password')
]
