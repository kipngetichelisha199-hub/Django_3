from django.db import models


# Create your models here.

class hobbies(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    dob=models.DateTimeField()
    weight=models.FloatField()
    image =models.CharField(max_length=255)

class Iterest(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    
    