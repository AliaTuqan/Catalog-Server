import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Book
from . serializer import bookSerializer, bookSerializer2

class bookList(APIView) :
    def get(self,request,topic_name):
        books_with_specific_topic = Book.objects.all().filter(topic=topic_name)
        serializer = bookSerializer(books_with_specific_topic, many=True)
        return Response(serializer.data)

class bookList2(APIView):
    def get(self,request,id):
        certain_book = Book.objects.all().filter(id=id)
        serializer = bookSerializer2(certain_book, many=True)
        return Response(serializer.data)
    def put(self,request,pk):
        certain_book = Book.objects.get(id=pk)
        certain_book.quantity -= 1
        certain_book.save()
