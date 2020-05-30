from django.db import models
from django import forms


class User(models.Model):
    age = models.IntegerField(max_length=200)
    job = models.CharField(max_length=100)
    file = models.FileField(null=True)

    # fields = ('age', 'job', 'file')


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
