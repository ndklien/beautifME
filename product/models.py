from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    # Ten spham
    product_name = models.CharField(max_length=255, blank=False, null=False)

    # Giai thich ve spham
    description = models.TextField()



    # Spham phu hop voi loai da nao (da dau, da kho, v.v.)
    SKINTYPE_CHOICE = [
        ('DRY', 'Dry Skin'), 
        ('OIL', 'Oliy Skin'),
        ('COMBI', 'Combination Skin'),
        ('ALL', 'All Skin Type'),
    ]

    skintype = models.CharField(max_length=5, choices=SKINTYPE_CHOICE)

    # Spham phu hop voi tinh trang da nao (bi mun, lao hoa, v.v.)
    SKINCOND_CHOICE = [
        ('SEN', 'Sensitive Skin'),
        ('ACNE', 'Acne Skin'), 
        ('AGE', 'Aging Skin'),
    ]

    skin_cond = models.CharField(max_length=5, choices=SKINCOND_CHOICE)

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
