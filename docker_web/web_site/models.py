from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=110)


class Container(models.Model):
    name = models.CharField(max_length=100)
    conid = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    port = models.CharField(max_length=100)


class Hostinfo(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    ip = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    islive = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    images = models.ManyToManyField(Images)
    container = models.ManyToManyField(Container)


class Group(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
