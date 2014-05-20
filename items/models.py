from django.db import models
from django.contrib import admin


class ItemTag(models.Model):
    title = models.CharField(max_length=1000, null=False)

    def __unicode__(self):
        return self.title


class ItemInstance(models.Model):
    # parent = models.ForeignKey("self", related_name="children", null=True)
    value = models.CharField(max_length=1000, null=True)
    complete = models.BooleanField(default=False, blank=False)
    start_time = models.TimeField(null=True)
    start_date = models.DateField(null=True)
    priority = models.IntegerField(null=True)

    def __unicode__(self):
        return self.value


class ItemTagValue(models.Model):
    tag = models.ForeignKey(ItemTag)
    value = models.CharField(max_length=1000)
    item = models.ForeignKey(ItemInstance)

    def __unicode__(self):
        return "%(item)s: %(tag)s - %(value)s" % ({'item': self.item, 'tag': self.tag, 'value': self.name})



# # Instance of a tag, tied to an item and a tag
# class ItemTagInstance(models.Model):
#     tag = models.ForeignKey(ItemTag)
#     item = models.ForeignKey(ItemInstance)
#     value = models.CharField(max_length=1000)
#
#     def __unicode__(self):
#         return "%(tag)s - %(value)s" % ({'tag': self.tag, 'value': self.value})




admin.site.register(ItemInstance)
admin.site.register(ItemTag)
admin.site.register(ItemTagValue)
