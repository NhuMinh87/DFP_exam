from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()

    return render(
        request,
        'books/book_list.html',
        {'books': books}
    )


def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price']
        )

        return redirect('/books/')

    return render(request, 'books/add_book.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.save()

        return redirect('/books/')

    return render(
        request,
        'books/edit_book.html',
        {'book': book}
    )


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('/books/')