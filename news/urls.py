from django.urls import path
from .views import NewsListView, NewsDetail

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:news_id>/<slug:slug>/', NewsDetail, name='news-detail')   
]