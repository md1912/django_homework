from django.db import models


class Book(models.Model):
    GENRE = (
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Fantasy", "Fantasy"),
        ("Manga", "Manga"),
        ("Romantic", "Romantic"),
        ("Action", "Action")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)

    def __str__(self):
        return self.title
