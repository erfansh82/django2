from operator import truth
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class document(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField(blank=True,null=True)

    class Meta:
        ordering=('title',)