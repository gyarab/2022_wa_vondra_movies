from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

def _str_(self):
    return f"{self.name} ({self.year})"