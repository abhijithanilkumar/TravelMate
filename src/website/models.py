from __future__ import unicode_literals
from profiles.models import Profile
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Stop(models.Model):
    LABEL = (('S','Source'),
             ('D','Destination'),
             ('I','Intermediate'),
             )
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    route = models.ForeignKey(Route, related_name='stops')
    label = models.CharField(max_length=1,choices=LABEL)

    def __str__(self):
        return self.name

class Pooling(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    route = models.OneToOneField(Route)
    seats = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Bus(models.Model):
    name = models.CharField(max_length=50)
    route = models.OneToOneField(Route)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.name

class BusDetail(models.Model):
    name = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    src = models.CharField(max_length=50)
    dst = models.CharField(max_length=50)
    srct = models.DateTimeField()
    dstt = models.DateTimeField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CarDetail(models.Model):
    name = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    src = models.CharField(max_length=50)
    dst = models.CharField(max_length=50)
    srct = models.DateTimeField()
    dstt = models.DateTimeField()
    seats = models.IntegerField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
