from os import times
from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.

class Gallery(models.Model):
    Images = models.FileField(upload_to= 'gallery')

class Events(models.Model):
    Title = models.CharField(max_length=100)
    description = models.TextField()
    Images = models.FileField(upload_to= 'events')


class LeaderShip(models.Model):
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Images = models.FileField(upload_to= 'events')


class Contact(models.Model):
    Email = models.EmailField()
    Phone = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()
    

