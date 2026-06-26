from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.URLField()
    guest = models.IntegerField()

    def __str__(self):
        return self.name
