from django.db import models
import datetime
from django.utils import timezone
from djrichtextfield.models import RichTextField

from django.urls import reverse

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    news_img = models.ImageField(upload_to='news/images/')
    pub_date = models.DateField(auto_now_add=True)
    summary = models.TextField(max_length=250)
    content = RichTextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news-detail', args=[str(self.id)])