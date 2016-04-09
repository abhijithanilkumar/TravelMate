from __future__ import unicode_literals
from profiles.models import Profile
from django.db import models

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
    route = models.ForeignKey(Route)
    label = models.CharField(max_length=1,choices=LABEL)

    def __str__(self):
        return self.name

class Pooling(models.Model):
    user = models.ForeignKey(Profile)
    route = models.OneToOneField(Route)

    def __str(self):
        return "%s %s" (self.user.get_full_name(),self.route.name)
