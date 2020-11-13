from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title