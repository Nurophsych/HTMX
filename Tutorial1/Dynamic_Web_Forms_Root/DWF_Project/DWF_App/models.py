from django.db import models

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=75)
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return self.name