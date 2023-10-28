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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
import csv
import pandas as pd
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
    

    
class UserCreate(APIView):
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
    

class MyPageNumberPagination(PageNumberPagination):
    page_size=6
    page_query_param='satyam'
    max_page_size=4

class BookFilterAPIView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [ SearchFilter]
    search_fields =['title']
    pagination_class=MyPageNumberPagination 
    

class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = BookSerializer(id)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = BookSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RecommendationAPIView(APIView):
    def post(self, request, format=None):
        category_name = request.data.get('category')
        books = Book.objects.filter(category__type__iexact=category_name)
        book_titles = [book.title for book in books]
        return Response({'books': book_titles})
    


# def venue_csv(request):
#         response = HttpResponse(content_type="text/csv")
#         response['Content-Disposition']='attachment; filename=somefilename.csv'

#         writer=csv.writer(response)

#         venues=Book.objects.all()

#         writer.writerow(['title','price','stock','published_date','category'])


#         for venue in venues:
#             writer.writerow([venue.title,venue.price,venue.stock,venue.published_date,venue.category])

#         return response


# def get_venue(request):
#     venues = Book.objects.all().values('title', 'price', 'stock', 'published_date', 'category')
#     df = pd.DataFrame.from_records(venues)

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=somefilename.csv'

#     df.to_csv(path_or_buf=response, index=False, header=['title', 'price', 'stock', 'published_date', 'category'])

#     return response

    