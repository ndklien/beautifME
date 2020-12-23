from django.shortcuts import render
from . import views
from .models import News

# Create your views here.
def listNews(request):
    list_news = News.objects.all()
    context = {"listnews": list_news}
    return render(request, "news/base_newsList.html", context)

def detailNews(request, news_id):
    t=News.objects.get(pk=news_id)
    return render(request, "news/base_newsDetail.html", {"t": t})


