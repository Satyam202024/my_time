from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class Role(models.Model):
    IS_ADMIN = 1
    IS_SUPERADMIN = 2
    IS_MEMBER = 3

    ROLE_CHOICES = (
        (IS_ADMIN, 'is_admin'),
        (IS_SUPERADMIN, 'is_superadmin'),
        (IS_MEMBER, 'is_member'),
    )
    ROLES_CHOICES = (
        ('IS_ADMIN', 'is_admin'),
        ('IS_SUPERADMIN', 'is_superadmin'),
        ('IS_MEMBER', 'is_member'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(
        max_length=100, choices=ROLES_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class User(AbstractUser):
    CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)
    username=None
    name=models.CharField(max_length=255,null=True, blank=True)
    contact=models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=255,choices=CHOICES)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, default=3)
    email=models.EmailField(unique=True)


    objects=UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS =[]

