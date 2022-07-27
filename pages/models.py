from datetime import date
from email.quoprimime import body_check
from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(max_length=255)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
