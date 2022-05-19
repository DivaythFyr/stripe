from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


