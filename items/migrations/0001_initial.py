# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemType'
        db.create_table(u'items_itemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'items', ['ItemType'])

        # Adding model 'ItemInstance'
        db.create_table(u'items_iteminstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['items.ItemInstance'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('item_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.ItemType'])),
        ))
        db.send_create_signal(u'items', ['ItemInstance'])

    def backwards(self, orm):
        # Deleting model 'ItemType'
        db.delete_table(u'items_itemtype')

        # Deleting model 'ItemInstance'
        db.delete_table(u'items_iteminstance')

    models = {
        u'items.iteminstance': {
            'Meta': {'object_name': 'ItemInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['items.ItemType']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': u"orm['items.ItemInstance']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'items.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['items']