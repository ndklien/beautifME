from django.contrib import admin
from django.urls import path, include
from .views import view_editProfile

app_name = 'accounts'

urlpatterns = [
    path('', view_editProfile, name='accounts-preview'),
]

