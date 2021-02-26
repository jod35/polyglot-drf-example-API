from django.db import models

# Create your models here.


class Subscriber(models.Model):
    name=models.CharField("Name",max_length=25)
    age=models.IntegerField("Age",null=False)
    email=models.CharField("Email",max_length=80,null=False)
