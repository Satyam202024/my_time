from django.db import models

# Create your models here.
class Upload(models.Model):
    title=models.CharField(max_length=40)
    file = models.FileField(upload_to='documents/')
