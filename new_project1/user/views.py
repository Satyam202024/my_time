from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
# Create your views here.
class UserView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
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
    
class UserViewList(APIView):
    def get(self, request, format=None):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



