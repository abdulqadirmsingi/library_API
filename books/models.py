from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    # published_date = models.DateField()
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # stock = models.IntegerField()
    # available = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
