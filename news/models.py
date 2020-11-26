from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    news_img = models.ImageField(upload_to='news/images/')
    pub_date = models.DateField(auto_now_add=True)
    summary = models.TextField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title