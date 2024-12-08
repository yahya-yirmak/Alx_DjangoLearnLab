from django.db import models

# Create your models here.


# The Book model represents a book in the system, including its title, publication year, and author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()  
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# The Author model represents an author who has written one or more books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
