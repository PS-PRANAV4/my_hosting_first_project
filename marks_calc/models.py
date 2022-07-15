from statistics import mode
from django.db import models

# Create your models here.
class author(models.Model):
    auther_name = models.CharField(max_length=25)


class marks(models.Model):
    mark_for  = models.CharField(max_length=25)
    confidence = models.FloatField()
    content = models.FloatField()
    fluency = models.FloatField()
    auther = models.ForeignKey(author,models.CASCADE)

    