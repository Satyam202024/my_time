from django.shortcuts import render
from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, login
# Create your views here.
class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return UserData.objects.get(pk=pk)
        except UserData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = UserSerializer(id)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateView(APIView):    
    def post(self, request, format=None):
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user) 
            return Response( {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user':serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'email':email}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
 

        