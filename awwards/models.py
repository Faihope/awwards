from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField


# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100,null=False)
    description=models.TextField(max_length=500)
    screenshot1=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    screenshot2=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    screenshot3=models.ImageField(default='default\.png',upload_to='screenshots/',blank=True)
    link=models.CharField(max_length=100,blank=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    bio = TextField(max_length=500,null=False)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name



