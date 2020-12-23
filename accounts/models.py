from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from django.db.models.signals import post_save
GENDER_CHOICE = [
        ('M', 'Male'), 
        ('F', 'Female')
]
    
SKINTYPE_CHOICE = [
        ('DRY', 'Dry Skin'), 
        ('OIL', 'Oliy Skin'), 
        ('COMBI', 'Combination Skin'),
        ('NORM', 'Normal Skin')
]

SKINCOND_CHOICE = [
        ('SEN', 'Sensitive Skin'),
        ('ACNE', 'Acne Skin'), 
        ('AGE', 'Aging Skin'),
]

#add to user profileS
class UserAccount(models.Model):
        #connect with django user account
        id_user = models.ForeignKey(User, on_delete=models.CASCADE)

        #user gender
        gender = models.CharField(max_length=2, choices=GENDER_CHOICE, null=True, blank=True)

        #user avatar
        userImg = models.ImageField(upload_to='accounts/images/', null=True, blank=True)
 
        def __str__(self):
                return User.__str__(self)
