from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','email','password']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__'
