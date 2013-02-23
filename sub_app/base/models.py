from django.db import models

# Create your models here.

class Base(models.Model):
    test = models.CharField(max_length=1000, blank=True)

class Some(models.Model):
    class Meta:
        db_table = 'ChangeName'
    test = models.CharField(max_length=1000, blank=True)

