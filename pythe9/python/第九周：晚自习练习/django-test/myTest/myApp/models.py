from django.db import models

# Create your models here.

class First(models.Model):
    name = models.CharField(max_length=200,unique=True)
    des = models.CharField(max_length=200)

    def __str__(self):
        return self.name