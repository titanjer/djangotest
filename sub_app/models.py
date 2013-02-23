from django.db import models

# Create your models here.

class Root(models.Model):
    name = models.CharField(max_length=1000, blank=True)
