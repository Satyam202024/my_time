from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from django.shortcuts import get_object_or_404
# Create your views here.
class FeedbackView(APIView):
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = FeedbackSerailizer(id)
        return Response(serializer.data)
    
    # def put(self, request, pk, format=None):
    #     instance = self.get_object(pk)
    #     serializer =FeedbackSerailizer(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BookFeedbackCountView(APIView):
    def get(self, request, book_id, format=None):
        book = get_object_or_404(Book, id=book_id)
        feedback_count = Feedback.objects.filter(title=book).count()
        average_rating = Feedback.objects.filter(title=book).aggregate(Avg('rating'))['rating__avg']
        book_data = {
            'book_name': book.title,
            'feedback_count': feedback_count,
            'average_rating': average_rating,
        }
        return Response(book_data)