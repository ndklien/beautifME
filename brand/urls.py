from django.urls import path
from . import views

app_name = 'brand'

urlpatterns = [
    path('', views.BrandList.as_view(), name='brand-list'),
    path('<int:brand_id>/', views.BrandPList, name='brandp_list'),
]