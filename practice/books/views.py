from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    #queryset tells which table to work with. Eg here Book
    #objects - it is the implicit field created by Django in the model that you've created (Book)
    #objects.all() means you are working in the entirety of data available
    #it can be used to modify the sample size of available data like..
    #queryset = Book.objects.filter(available=True) -> will only work with certain books(available ones)
    #this is equivalent of telling SpringBoot which repository(table) we are working with..
    #not Author but Book (In SpringBoot -> BookRepository bookRepository object would have conveyed this info..
    #which also provided some inbuilt CRUD functions)
    queryset = Book.objects.all()

    serializer_class = BookSerializer


    # If detail=False, it applies to the entire collection (e.g., /books/by-author/7/)
    # If detail=True, it would apply to a specific book (e.g., /books/5/by-author/).

    # methods : PLURAL : could be - methods=['get', 'post'] : function can serve both needs depending on request type and body
    # if request.method == "GET":
    # elif request.method == "POST":

    # request is a HTTP request object. Has all info.

    # Response is similar to ResponseEntity in Spring Boot

    # BookSerializer(books, many=True) converts the books(Django model instances) into a Python dictionary (which DRF then converts to JSON).

    # Response(serializer.data, status=status.HTTP_200_OK) --> Response(serializer.data, staus=200) : Both work fine but 1st is better practice

    @action(detail=False, methods=['get'], url_path='by-author/(?P<author_id>\d+)')
    def books_by_author(self, request, author_id=None):
        try:
            books = Book.objects.filter(authorId=author_id)
            if not books.exists():
                return Response({"message": "No books found for this author"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




