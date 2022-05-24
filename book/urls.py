from django.urls import path
from . import views
app_name = "books_url"
urlpatterns = [
    path('books/', views.all_books , name="books_all_url"),
    path('books/<int:id>/', views.get_book_detail, name="books"),
    path('add-books/', views.add_book, name="add_books"),
    path('books/latest/', views.book_latest, name="latest"),
    path('books/drama/', views.book_drama, name="drama"),
    path('books/horror/', views.book_horror, name="horror"),
    path('books/comedy/', views.book_comedy, name="comedy"),
    path('books/fantasy/', views.book_fantasy, name="fantasy"),
    path('books/manga/', views.book_manga, name="manga"),
    path('books/romantic/', views.book_romantic, name="romantic"),
    path('books/action/', views.book_action, name="action"),
    path('books/<int:id>/update/', views.book_update, name="show_update"),
    path('books/<int:id>/delete/', views.book_delete, name="show_delete"),
]
