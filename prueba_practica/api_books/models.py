from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=20)
    pages_number = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    books = models.ManyToManyField("Books", verbose_name = ("Libros"), null=True, blank=True)
    
        
    def __str__(self):
        return self.name
    