from django.urls import path
from .views import (
    book_list,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:id>/', edit_book, name='edit_book'),
    path('delete/<int:id>/', delete_book, name='delete_book'),
]