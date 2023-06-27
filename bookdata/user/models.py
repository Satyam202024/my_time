from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)

    objects=UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =[]


class Category(models.Model):
    type = models.CharField(max_length=30 ,blank=True ,null=True)

    def __str__(self):
        return self.type

class Book(models.Model):
    title=models.CharField(max_length=40,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    stock=models.IntegerField(blank=True,null=True)
    published_date=models.DateField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title