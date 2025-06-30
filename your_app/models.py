from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
    ('G', 'Games'),
    ('SO', 'Software'),
    ('M', 'Movies'),
)

def userprofile_receiver(_sender, instance, created, *_, **__):
    if created:
        UserProfile.objects.create(user=instance)