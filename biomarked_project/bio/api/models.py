from django.db import models

# Create your models here.
CHOICES = (
        ('amazon', 'Amazon'),
        ('flipkart', 'Flipkart'),
    )

class ProductType(models.Model):
    product_name=models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return str(self.product_name)

class Biomarked(models.Model):
    platform=models.CharField(max_length=50,choices=CHOICES)
    name=models.CharField(max_length=50,null=True, blank=True)
    link=models.CharField(max_length=50,null=True, blank=True)
    i_frame=models.CharField(max_length=50,null=True, blank=True)
    status=models.BooleanField(default=False)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
        return str(self.name)
    
