from django.db import models

class Employe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    dgs = models.CharField(max_length=30)
    salary = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=40)