from django.db import models
from django.contrib import admin

class ItemType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class ItemInstance(models.Model):
    parent = models.ForeignKey("self", related_name="children", null=True)
    value = models.CharField(max_length=1000, null=True)
    item_type = models.ForeignKey(ItemType, null=False)

    def __unicode__(self):
        return self.value

admin.site.register(ItemInstance)
admin.site.register(ItemType)
