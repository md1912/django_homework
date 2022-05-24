from .models import Book
from . import forms
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from datetime import datetime, timedelta


def all_books(request):
    books = Book.objects.all()
    return render(request, "book.html", {"books": books})


def get_book_detail(request, id):
    object = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": object})

# def tv_show(request):
#     queryset = models.Shows.objects.order_by("-id")
#     return render(request, "shows_all.html", {"shows": queryset})
#
def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("TVShow Created successfully")
            return redirect(reverse("books_url:books_all_url"))
    else:
        form = forms.BookForm()
    return render(request, "add_book.html", {"form": form})


start_date = datetime.today() - timedelta(days=5)
def book_delete(request, id):
     book_delete = get_object_or_404(Book, id=id)
     book_delete.delete()
     return redirect(reverse("books_url:books_all_url"))
#


def book_latest(request):
    queryset = Book.objects.filter(created_date__gt=start_date).order_by("-id")
    return render(request, "book.html", {"books": queryset})


def book_drama(request):
    queryset = Book.objects.filter(genre="Drama").order_by("-id")
    return render(request, "book.html", {"books": queryset})


def book_horror(request):
    queryset = Book.objects.filter(genre="Horror").order_by("-id")
    return render(request, "book.html", {"books": queryset})
#
def book_comedy(request):
    queryset = Book.objects.filter(genre="Comedy").order_by("-id")
    return render(request, "book.html", {"books": queryset})

def book_fantasy(request):
    queryset = Book.objects.filter(genre="Fantasy").order_by("-id")
    return render(request, "book.html", {"books": queryset})#
#

def book_manga(request):
    queryset = Book.objects.filter(genre="Manga").order_by("-id")
    return render(request, "book.html", {"books": queryset})#

def book_romantic(request):
    queryset = Book.objects.filter(genre="Romantic").order_by("-id")
    return render(request, "book.html", {"books": queryset})

def book_action(request):
    queryset = Book.objects.filter(genre="Action").order_by("-id")
    return render(request, "book.html", {"books": queryset})

def book_update(request, id):
    book_object = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books_url:books_all_url"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, "book_update.html", {"form": form,
                                                "object": book_object})

