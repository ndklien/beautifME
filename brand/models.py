from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Brand(models.Model):
    BRANDING = [
        ('KIE', "Kielh's"),
        ('INN', 'Innisfree'),
        ('BIO', 'Biore'),
        ("BUR", "Burberry"),
        ('CET', 'Cetaphil'),
        ('CER', 'Cerave'),
        ('CLI', 'Clinique'),
        ('COO', 'Cocoon'),
        ('DHC', 'DHC'),
        ('EST', 'Estee Lauder'),
        ('ACN', 'Acnes'),
        ('HAD', 'Hada Labo'),
        ('HUX', 'Huxley'),
        ('LAR', 'La roche Posay'),
        ('LAN', 'Lancome'),
        ('LOR', 'Loreal'),
        ('MIS', 'Missha'),
        ('MUR', 'Murad'),
        ('NEU', 'Neutrogena'),
        ('OMI', 'Omi'),
        ('OHU', 'Ohui'),
        ('PAU', "Paula's Choice"),
        ('SEN', 'Senka'),
        ('SIM', 'Simple'),
        ('SOM', 'Some by Mi'),
        ('SUL', 'Sulwhasoo'),
        ('THA', "Thayer's"),
        ('VAS', 'Vaseline'),
        ('SK2', 'SKII'),
        ('LAM', 'La Mer'),
        ('ELE', 'Drunk Elephant'), 
        ('FRE', 'Fresh'),
        ('TAT', 'Tatcha'),
        ('ORD', 'The Ordinary'),
        ('GLO', 'Glossier'),
        ('BDM', 'Bioderma'),
    ]

    branding_name = models.CharField(max_length=3, choices=BRANDING)

    brand_img = models.ImageField(upload_to='brand/images/')

    #Branding Category: Trending, Highend, Drugstore
    BRAND_CAT = [
        ('TREN', 'On Trending'), 
        ('HIGH', 'high-end Products'),
        ('DRUG', 'Drugstore Products'),
    ]

    brand_cat = models.CharField(max_length=4, choices=BRAND_CAT, null=True, blank=True)

    brandDescript = models.TextField()

    #slugField for brandname endpoint
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.branding_name

    def slug(self):
        return slugify(self.branding_name)