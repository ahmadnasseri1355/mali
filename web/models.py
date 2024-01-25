from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
	text = models.CharField(max_length=255)
	date = models.DateTimeField(default=timezone.now)
	amount = models.BigIntegerField(default=0)
	user = models.ForeignKey(User,default=None,null=True,on_delete=models.SET_NULL,related_name="expenses",verbose_name="خریدار")

class Incomes(models.Model):
	text = models.CharField(max_length=255)
	date = models.DateTimeField(default=timezone.now)
	amount = models.BigIntegerField(default=0)
	user = models.ForeignKey(User,default=None,null=True,on_delete=models.SET_NULL,related_name="incomes")
