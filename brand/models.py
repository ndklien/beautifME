from django.db import models
from django.template.defaultfilters import slugify

from multiselectfield import MultiSelectField

# Create your models here.
class Brand(models.Model):
    # branding_name = models.CharField(max_length=3, choices=BRANDING)
    branding_name = models.CharField(max_length=255, unique=True)

    brandImage = models.ImageField(upload_to='brand/images/')

    #Branding Category: Trending, Highend, Drugstore
    BRAND_CAT = [
        ('TREN', 'On Trending'), 
        ('HIGH', 'High-end Products'),
        ('DRUG', 'Drugstore Products'),
    ]

    # brand_cat = models.CharField(max_length=4, choices=BRAND_CAT, null=True, blank=True)
    brandCategory = MultiSelectField(choices=BRAND_CAT, null=True, blank=True)

    brandDescript = models.TextField()

    #slugField for brandname endpoint
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.branding_name

    def slug(self):
        return slugify(self.branding_name)