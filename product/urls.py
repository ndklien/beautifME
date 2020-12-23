from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:product_id>/', views.productDetail, name='product-detail'),
]