from django.db import models

class Blogger(models.Model):
    data = models.DateField()
    description = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title