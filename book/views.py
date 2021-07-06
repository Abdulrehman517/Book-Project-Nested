from . import models, serializers
from .models import Book, BookDetails
from rest_framework.views import APIView
from .serializers import BookSerializer, BookDetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .models import Book

class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Book.objects.all()
#     serializer_class = serializers.BookSerializer
# class BookDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         if request.method == 'GET':
#                 book = Book.objects.get(pk=pk)
#                 serializer = BookSerializer(book)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response({serializer.data}, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         if request.method == 'PUT':
#             book = Book.objects.get(pk=pk)
#             serializer = BookSerializer(book, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#
#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
