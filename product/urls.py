from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:product_id>/<slug:slug>/', views.productDetail, name='product-detail'),
]