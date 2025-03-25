from django.shortcuts import render
from rest_framework import viewsets
from models import Book,Author
from serializers import BookSerializer,AuthorSerializer

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


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




