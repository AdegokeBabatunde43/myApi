from email.quoprimime import body_check
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(max_length=255)
    completed=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
