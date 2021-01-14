from django.db import models

# Create your models here.
class book_shelf(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    edition = models.IntegerField(max_length=5, null=True, blank=True)
    price = models.IntegerField(max_length=8, null=True, blank=True)
    
