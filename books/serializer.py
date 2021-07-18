from rest_framework import serializers
from books.models import Book
class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title')
class bookSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'quantity', 'price')
