from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.listNews, name='news-list'),
    path('<int:news_id>/', views.detailNews, name='news-detail'),
]