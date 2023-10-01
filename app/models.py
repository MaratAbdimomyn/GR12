from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=40)
    value = models.IntegerField()
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.name