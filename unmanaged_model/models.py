from django.db import models

# Create your models here.

class Unmanaged(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = u'unmanaged'
