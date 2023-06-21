from rest_framework import serializers
from .models import *
class UpoadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields=['id','title','file']
