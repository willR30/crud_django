from django.db import models

# Create your models here.

class Animal(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500, default="None")

    def __str__(self):
        return f'{self.id}-{self.name}, {self.details}'
