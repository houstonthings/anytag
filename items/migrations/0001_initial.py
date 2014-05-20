# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemTag'
        db.create_table(u'items_itemtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'items', ['ItemTag'])

        # Adding model 'ItemInstance'
        db.create_table(u'items_iteminstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'items', ['ItemInstance'])

        # Adding model 'ItemTagValue'
        db.create_table(u'items_itemtagvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.ItemTag'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.ItemInstance'])),
        ))
        db.send_create_signal(u'items', ['ItemTagValue'])


    def backwards(self, orm):
        # Deleting model 'ItemTag'
        db.delete_table(u'items_itemtag')

        # Deleting model 'ItemInstance'
        db.delete_table(u'items_iteminstance')

        # Deleting model 'ItemTagValue'
        db.delete_table(u'items_itemtagvalue')


    models = {
        u'items.iteminstance': {
            'Meta': {'object_name': 'ItemInstance'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'items.itemtag': {
            'Meta': {'object_name': 'ItemTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'items.itemtagvalue': {
            'Meta': {'object_name': 'ItemTagValue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.ItemInstance']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.ItemTag']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['items']