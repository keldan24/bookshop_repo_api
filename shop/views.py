from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serial import Bookserializers
from. models import Book


# Create your views here.

@api_view(['GET'])
def books(req):
    all_books = Book.objects.all()
    serialized_data = Bookserializers(all_books, many= True)
    return Response(serialized_data.data)


@api_view(['GET'])
def books_by_author(req, author):
    all_books = Book.objects.filter(author__iexact= author)
    serialized_data = Bookserializers(all_books, many= True)
    return Response(serialized_data.data)


@api_view(['GET'])
def books_by_id(req, id):
    all_books = Book.objects.get(id=id)
    serialized_data = Bookserializers(all_books)
    return Response(serialized_data.data)



@api_view(['POST'])
def add_book(req):

    serialized_data = Bookserializers(data=req.data)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)



@api_view(['DELETE'])
def delete_book(req):

    serialized_data = Bookserializers(data=req.data)
    if serialized_data.is_valid():
        serialized_data.delete()
    return Response(serialized_data.data)



@api_view(['PATCH'])
def patch_book(req):

    serialized_data = Bookserializers(data=req.data)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)



@api_view(['PUT'])
def put_book(req):

    serialized_data = Bookserializers(data=req.data)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)