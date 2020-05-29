from django.db import models

class User(models.Model):
    age = models.IntegerField(max_length=200)
    job = models.CharField(max_length=100)
    file = models.FileField(null=True)

    # fields = ('age', 'job', 'file')
