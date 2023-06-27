from rest_framework import serializers
from .models import Biomarked

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biomarked 
        fields = '__all__'