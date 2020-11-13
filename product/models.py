from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Product(models.Model):
    # Ten spham
    product_name = models.CharField(max_length=255, blank=False, null=False)

    # Giai thich ve spham
    description = models.TextField()

    # Gia spham
    price = models.IntegerField(default=0)

    # Spham phu hop voi loai da nao (da dau, da kho, v.v.)
    skintype = models.ValueRange()

    # Spham phu hop voi tinh trang da nao (bi mun, lao hoa, v.v.)
    skin_cond = models.CharField(max_length=50)

    # Binh chon yeu/ghet spham
    vote_down = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)

    # Loai san pham: SRM, Toner, v.v.
    category = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    #comment thuoc product nao
    product = models.ForeignKey('Product', on_delete=models.CASCADE) 

    #comment cua user nao
    
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
