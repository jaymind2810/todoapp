from typing import Text
from django.db import models
from django.shortcuts import render

# Create your models here.
class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
def __str__(self):
    return self.text