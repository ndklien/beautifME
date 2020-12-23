from django.contrib import admin
from django.urls import path, include
from .views import view_editProfile

app_name = 'accounts'

<<<<<<< HEAD
=======
urlpatterns = [
    path('', view_editProfile, name='accounts-preview'),
]
>>>>>>> 095fb8ca72d7a430fb26576d9c1934e7dfa5adbe

