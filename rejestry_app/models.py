from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import timezone


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(
        default=timezone.now
    )
    body = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.body


class Pet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(max_length=255)

class Rejestr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa_pelna = models.CharField(max_length=255)
    nazwa_skrocona = models.CharField(max_length=50)
    dysponent_id = models.CharField(max_length=255)
    podstawa_prawna = models.CharField(max_length=1000)
    przeznaczenie = models.CharField(max_length=1000)
    zakres_info = models.CharField(max_length=1000)
    zakres_lista = models.CharField(max_length=200)



