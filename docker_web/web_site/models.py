from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=110)


class Container(models.Model):
    name = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    images = models.ManyToManyField(Images)
    container = models.ManyToManyField(Container)


class Group(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
