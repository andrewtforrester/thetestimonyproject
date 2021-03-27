from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    majors = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    text = models.TextField()

    def __str__(self):
        return self.author.first_name + " " + self.author.last_name + ": " + self.title
