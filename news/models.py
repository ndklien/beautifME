from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

from django.urls import reverse
# Rich Text Field
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    news_img = models.ImageField(upload_to='news/static/news/images/')
    pub_date = models.DateField(auto_now_add=True)
    summary = models.TextField(max_length=250)
    content = RichTextUploadingField(null=True, blank=True)

    #slugField for news endpoint
    slug = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news-detail', args=[str(self.id), self.slug])

    # def slug(self):
    #     return slugify(self.slug)