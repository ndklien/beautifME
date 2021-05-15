from django.shortcuts import render
from django.views import generic

from . import views
from .models import News

# Create your views here.
""" List of news in the News section """
class NewsListView(generic.ListView):
    model = News
    template_name = 'news/base_newsList.html'
    context_object_name = 'news_list'
    paginate_by = 5
    def get_queryset(self):
        return News.objects.order_by('-pub_date')


""" One Article preview """
def NewsDetail(request, news_id, slug):
    current_news = News.objects.get(pk=news_id)
    context = {
        'current_news': current_news,
    }
    return render(request, 'news/base_newsDetail.html', context)
