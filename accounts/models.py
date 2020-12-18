from django.db import models
from django.contrib.auth.models import User

from django import forms

GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female'),
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

# Create your models here.
class addAccountsForm(forms.Form):

    #user gender
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE)

    #user skintype
    skintype = models.CharField(max_length=5, choices=SKINTYPE_CHOICE)

    #user skin condition
    skincondition = models.CharField(max_length=5, choices=SKINCOND_CHOICE, null=True, blank=True)

    userImg = models.ImageField(upload_to='accounts/images/')

    def __str__(self):
        return User.__str__(self)
