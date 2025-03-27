from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Author(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=50,default="Author_name")
    place=models.CharField(max_length=50, default='Author_place')

    def __str__(self):
        return self.name+" ,"+self.place


class Book(models.Model): #models.Model : Registers it with Django’s ORM

    # objects = models.Manager() #No need to write this
                                 #It is used to create custom Manager (Manager handles CRUD in DB)
                                 #by custom Manager I mean like if you want to search and all differently
                                 #but I've written this down since Pycharm doesn't find this field when used in views

    objects=models.Manager()
    id=models.AutoField(primary_key=True) # By default its integer
    name=models.CharField(max_length=200)
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE) #Default mapping is done to the primary key attribute of Author, but can be customised
    authorName=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    addedOnDate=models.DateTimeField(auto_now_add=True) #auto_now : Sets the field only once, when the object is first created.
    modifiedOnDate=models.DateTimeField(auto_now=True) #auto_now : Updates the field every time the object is saved (updated).
    genre=models.CharField(max_length=100,choices=( #max_length prevents storing longer, invalid values manually (e.g., via direct DB access).
                           ("Self Help","Self Help"),
                           ("Technology","Technology"),
                           ("Humanities","Humanities"),
                           ("Literature","Literature")
    ))


    def __str__(self):
        return self.name+" ,"+self.authorName













