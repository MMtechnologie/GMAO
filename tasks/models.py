from django.db import models


# Create your models here.
class Machine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=10)


class Panne(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    state = models.CharField(max_length=10)


class Curative(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    timestop = models.TimeField(auto_now_add=True)
    panne = models.ForeignKey(Panne, on_delete=models.CASCADE)
