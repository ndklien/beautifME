from django.urls import path
from . import views
import product.views as ProductV

app_name = 'brand'

urlpatterns = [
    path('', views.BrandList.as_view(), name='brand-list'),
    path('<int:brand_id>/', views.BrandPList, name='brandp-list'),
]