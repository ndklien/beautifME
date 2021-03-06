from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

from brand.models import Brand

from django.template.defaultfilters import slugify

# Multiple Choice Field
from multiselectfield import MultiSelectField
# Rich Text Field
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from djrichtextfield.models import RichTextField
#pip install Pillow for image import

# CK Editor
from ckeditor.fields import RichTextField

# Create your models here.

SKINCOND_CHOICE = (
    ('SEN', 'Sensitive Skin'),
    ('ACNE', 'Acne Skin'), 
    ('AGE', 'Aging Skin'),
    ('DULL', 'Dull Skin'),
    ('FREC', 'Freckles'),
)

CATEGORY_CHOICE = (
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
    ('MIST', 'Mist Spray'),
    ('OIL', 'Oil Moisturizing'),
    ('PERFUME', 'Perfume'),
    ('BODY', 'Body Care'),
    ('HAIR', 'Hair Care'),
)

SKINTYPE_CHOICE = (
    ('DRY', 'Dry Skin'), 
    ('OIL', 'Oily Skin'),
    ('COMBI', 'Combination Skin'),
    ('NORM', 'Normal Skin'),
)


class Product(models.Model):
    # Ten spham
    product_name = models.CharField(max_length=80, blank=False, null=False)

    #ten hang KEY 3 CHU DAU
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)

    #tom tat spham
    summary = models.TextField(max_length=300, blank=False, null=False)

    # Giai thich ve spham
    #description = RichTextField()
    description = RichTextUploadingField(blank=True, null=True)

    #dung tich san pham
    product_size_in_ml = models.IntegerField(default=0, null=False) 

    #hinh minh hoa spham
    product_img = models.ImageField(upload_to='product/images/')

    # Gia spham
    price = models.CharField(default=0, max_length=7)

    # Spham phu hop voi loai da nao (da dau, da kho, v.v.)
    skinType = MultiSelectField(choices=SKINTYPE_CHOICE, null=True, blank=True)

    # Spham phu hop voi tinh trang da nao (bi mun, lao hoa, v.v.)
    skinCondition = MultiSelectField(choices=SKINCOND_CHOICE, null=True, blank=True)

    # Loai san pham: SRM, Toner, v.v.
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE, blank=True, null=True)

    # Binh chon yeu/ghet spham
    vote_down = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)

    #slugField for endpoint
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return str(self.product_name)

    def get_absolute_url(self):
        slug = slugify(self.product_name)
        return reverse('product:product-detail', args=[str(self.id), slug])
        #return reverse('product:product-detail', args=[str(self.id)])

    def slug(self):
        return slugify(self.product_name)

class Comment(models.Model):
    #comment thuoc product nao
    product = models.ForeignKey('Product', on_delete=models.CASCADE) 

    #comment cua user nao
    # owner_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #Tua de cua comment
    title = models.CharField(max_length=255, blank=True, null=True)

    #Noi dung comment
    content = models.TextField()
    #thoi gian dang bai
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # Binh chon yeu/ghet binh luan
    vote_down = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)
