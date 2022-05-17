from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    books = Book.objects.all()
    return render(request, "book.html", {"books": books})

def get_book_detail(request, id):
    object = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": object})
