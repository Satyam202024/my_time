from django.db import models
from django.conf import settings
from django.db.models import Max
# Create your models here.

class Team(models.Model):
    name=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "team"


class Member(models.Model):
    t_name= models.ForeignKey(Team, on_delete=models.CASCADE)
    member=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)
    
    status=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.t_name} - {self.member}"
    
    class Meta: 
        db_table = "members"

class BillMember(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0)
    # import pdb
    # pdb.set_trace()
    def __str__(self):
        return f"{self.member} - {self.position}"
    def save(self, *args, **kwargs):
        if not self.position:
            max_position = BillMember.objects.aggregate(Max('position'))['position__max']
            if max_position is None:
                self.position = 1
            else:
                self.position = max_position + 1
        
        super().save(*args, **kwargs)

    class Meta: 
        db_table = "billmembers"
        


   
    