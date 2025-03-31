from django.db import models

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=75)
    information = models.TextField()
    

    def __str__(self):
        return self.name