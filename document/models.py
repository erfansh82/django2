from turtle import title
from django.db import models
 

class document(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True,null=True)

    class Meta:
        ordering=('title',)