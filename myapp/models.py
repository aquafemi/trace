from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Trace(models.Model):
    image = models.ImageField(upload_to='documents/%Y/%m/%d')

class AudioFile(models.Model):
    audio_file = models.FileField(upload_to='documents/%Y/%m/%d')
    length = models.FloatField(null=True)
    trace = models.ForeignKey(Trace, null=True)
