from django.db import models


# Create your models here.

class hobbies(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    dob=models.DateTimeField()
    weight=models.FloatField()
    image =models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
    