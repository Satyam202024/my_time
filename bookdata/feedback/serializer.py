from rest_framework import serializers
from .models import *
class FeedbackSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'