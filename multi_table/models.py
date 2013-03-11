# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals

# Create your models here.

class CustomManager(models.Manager):
    ''' Use this manager to get objects that have a canceled field ''' # {{{
    def get_query_set(self):
        return super(CustomManager, self).get_query_set().filter(canceled=False)
    def all_with_canceled(self):
        return super(CustomManager, self).get_query_set()
    def canceled_set(self):
        return super(CustomManager, self).get_query_set().filter(canceled=True)
    def get(self, *args, **kwargs):
        ''' if a specific record was requested, return it even if it's deleted '''
        return self.all_with_canceled().get(*args, **kwargs)
    def filter(self, *args, **kwargs):
        ''' if pk was specified as a kwarg, return it even if it's deleted '''
        if 'pk' in kwargs:
            return self.all_with_canceled().filter(*args, **kwargs)
        return self.get_query_set().filter(*args, **kwargs)
    def date_ranges(self, start=None, end=None, tag=None, *args, **kwargs):
        pass
        #date_start = date_end = None

        ##try:
        #if tag is None: date_start, date_end = parse_date_range(start, end)
        #else: date_start, date_end = parse_date_tag(tag=tag)

        #if date_end is None: # for one day
        #    return self.filter(date=date_start)
        #elif date_start < date_end:
        #    return self.filter(date__gte=date_start, date__lt=date_end)
        #else:
        #    return self.filter(date=date.today())
        ##except:
        ##    return self.filter(date=date.today())

    # }}}


class CustomModel(models.Model):
    version = models.PositiveIntegerField(default=0, null=True, blank=True)
    canceled = models.BooleanField(default=False, db_index=True)
    objects = CustomManager()
    class Meta:
        abstract = True


def custom_update_fields(instance, **kwargs):
    ''' ''' # {{{
    if isinstance(instance, models.Model):
        version = instance.version
        if instance.version is None:
            version = 1
        else:
            version = instance.version+1
        success = instance.__class__.objects.filter(pk=instance.id, version=instance.version).update(version=version, **kwargs)
        if not success:
            raise Exception('此筆資料儲存前, 已被更改過, 修改失敗!!')

        #
        instance.version = version
        for key, value in kwargs.iteritems():
            setattr(instance, key, value)

        signals.post_save.send(sender=instance.__class__, instance=instance, created=False)

        return True
    return False
    # }}}


def custom_update_model(instance):
    ''' ''' # {{{
    if isinstance(instance, models.Model):
        fields = dict([(f.name, getattr(instance, f.attname)) for f in instance._meta.fields])
        if instance.version is None:
            fields['version'] = version = 1
        else:
            fields['version'] = version = instance.version+1
        success = instance.__class__.objects.filter(pk=instance.id, version=instance.version).update(**fields)
        if not success:
            raise Exception('此筆資料儲存前, 已被更改過, 修改失敗!!')

        instance.version = version
        signals.post_save.send(sender=instance.__class__, instance=instance, created=False)

        return True
    return False

    # }}}


class Place(CustomModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()
