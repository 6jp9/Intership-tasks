from django.db import models
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=30)
    address= models.TextField(max_length=50)
