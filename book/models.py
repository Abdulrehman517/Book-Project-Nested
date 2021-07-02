from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class BookDetails(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='rbook')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
