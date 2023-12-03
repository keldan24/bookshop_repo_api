from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("books_add/", views.add_book),
    path("books/", views.books),
    path("books/<str:author>", views.books_by_author),
    path("book/<int:id>", views.books_by_id)
]