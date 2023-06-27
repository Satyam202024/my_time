from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import *
from .serializer import BioSerializer
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class BioViews(APIView):
    def get_object(self, pk):
        try:
            return Biomarked.objects.get(pk=pk)
        except Biomarked.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = BioSerializer(id)
        return Response(serializer.data)
    

class BioSearchView(ListAPIView):
    queryset=Biomarked.objects.all()
    serializer_class = BioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['name','type']