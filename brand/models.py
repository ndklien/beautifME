from django.db import models

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
        ('SOM', 'Sum by Mi'),
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
    ]

    branding_name = models.CharField(max_length=3, choices=BRANDING)

    brand_img = models.ImageField(upload_to='brand/static/brand/images/)

    brandDescript = models.TextField()

    def __str__(self):
        return self.branding_name