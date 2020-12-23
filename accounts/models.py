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

# Create your models here.
<<<<<<< HEAD
# class addAccountsForm(models.Model):

#     #user gender
#     gender = models.CharField(max_length=2, choices=GENDER_CHOICE)

#     #user skintype
#     skintype = models.CharField(max_length=5, choices=SKINTYPE_CHOICE)

#     #user skin condition
#     skincondition = models.CharField(max_length=5, choices=SKINCOND_CHOICE, null=True, blank=True)

#     userImg = models.ImageField(upload_to='accounts/images/')

#     def __str__(self):
#         return User.__str__(self)

class UserProfile(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        #user gender
        gender = models.CharField(max_length=2, choices=GENDER_CHOICE)

        #user skintype
        skintype = models.CharField(max_length=5, choices=SKINTYPE_CHOICE)

        #user skin condition
        skincondition = models.CharField(max_length=5, choices=SKINCOND_CHOICE, null=True, blank=True)

        userImg = models.ImageField(upload_to='accounts/images/')
        
        USERNAME_FIELD = 'userImg'

#add to user profileS
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
=======
class UserAccount(models.Model):
        #connect with django user account
        id_user = models.ForeignKey(User, on_delete=models.CASCADE)

        #user gender
        gender = models.CharField(max_length=2, choices=GENDER_CHOICE, null=True, blank=True)

        #user avatar
        userImg = models.ImageField(upload_to='accounts/images/', null=True, blank=True)
 
        def __str__(self):
                return User.__str__(self)
>>>>>>> 095fb8ca72d7a430fb26576d9c1934e7dfa5adbe
