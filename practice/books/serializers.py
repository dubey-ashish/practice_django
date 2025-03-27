from rest_framework import serializers
from .models import Book,Author

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields="__all__"

        # Without the Meta class, Django won't know:
        # ->Which model to serialize (model attribute).
        # ->Which fields to include (fields attribute).

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Author
        fields="__all__"