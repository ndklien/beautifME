from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

#pip install Pillow for image import

# Create your models here.


class Product(models.Model):
    # Ten spham
    product_name = models.CharField(max_length=50, blank=False, null=False)

    #ten hang KEY 3 CHU DAU
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
<<<<<<< HEAD
        ('THA', 'Thayes'),
=======
        ('THA', "Thayer's"),
>>>>>>> f581494ef6cf3704b4e0ac938bc3aa15185ba988
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

    #tom tat spham
    summary = models.CharField(max_length=100, blank=False, null=False)

    # Giai thich ve spham
    description = models.TextField()

    #dung tich san pham
    product_size_in_ml = models.IntegerField(default=0, null=False) 

    #hinh minh hoa spham
    product_img = models.ImageField(upload_to='product/images/')

    # Gia spham
    price = models.IntegerField(default=0)

    # Spham phu hop voi loai da nao (da dau, da kho, v.v.)
    SKINTYPE_CHOICE = [
        ('DRY', 'Dry Skin'), 
        ('OIL', 'Oliy Skin'),
        ('COMBI', 'Combination Skin'),
        ('NORM', 'Normal Skin'),
        ('ALL', 'All Skin Type'),
    ]

    skintype = models.CharField(max_length=5, choices=SKINTYPE_CHOICE)

    # Spham phu hop voi tinh trang da nao (bi mun, lao hoa, v.v.)
    SKINCOND_CHOICE = [
        ('SEN', 'Sensitive Skin'),
        ('ACNE', 'Acne Skin'), 
        ('AGE', 'Aging Skin'),
    ]

    skin_cond = models.CharField(max_length=5, choices=SKINCOND_CHOICE, null=True)

    # Loai san pham: SRM, Toner, v.v.
    CATEGORY_CHOICE = [
        ('MAKEUP_RM', 'Makeup Remover'),
        ('CLEANSE', 'Cleanser'),
        ('TONER', 'Toner'),
        ('SERUM', 'Serum'),
        ('MOIST', 'Moisturizer'),
        ('LOTION', 'Lotion'),
        ('MASK', 'Mask'),
        ('EYE', 'Eye Care'),
        ('SUN', 'Sun Care'),
        ('EXFOL', 'Exfoliators'),
        ('LIP', 'Lip Treatment'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE)

    # Binh chon yeu/ghet spham
    vote_down = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    #comment thuoc product nao
    product = models.ForeignKey('Product', on_delete=models.CASCADE) 

    #comment cua user nao
    owner_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    #Tua de cua comment
    title = models.CharField(max_length=255, blank=False, null=False)

    #Noi dung comment
    content = models.TextField()
    #thoi gian dang bai
    pub_date = models.DateTimeField(default=timezone.datetime.now())
    
    # Binh chon yeu/ghet binh luan
    vote_down = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)

    def __str__(self):
        return self.title
