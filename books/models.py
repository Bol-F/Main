from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=225)
    birth_date = models.DateField()

class Meta:
    db_table = 'author'
    ordering = '-birth_date'


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='')
