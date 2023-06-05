from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Station(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    contador = models.IntegerField()
    empty_slots = models.IntegerField()
    name = models.CharField(max_length=255)
    free_bikes = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    address = models.CharField(max_length=255)
    normal_bikes = models.IntegerField()
    payment = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['contador']

class Keypay(models.Model):
    station = models.OneToOneField(Station, primary_key=True, on_delete=models.CASCADE)
    metodos = ArrayField(models.CharField(max_length=64, null=True), size=5, null=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Keypay: {self.name}"



# class Project(models.Model):  #+ Le digo que cree una tabla llamada proyect 
#     name = models.CharField( max_length = 255 )

# class Task(models.Model):
#     title = models.CharField(max_length = 255)
#     description = models.TextField()
#     project = models.ForeignKey(Project, on_delete = models.CASCADE)