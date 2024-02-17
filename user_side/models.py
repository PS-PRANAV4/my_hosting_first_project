from django.db import models
from admins.models import Accounts
# Create your models here.
class Otp(models.Model):
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)
    