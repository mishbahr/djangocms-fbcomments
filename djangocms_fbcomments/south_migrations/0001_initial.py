# -*- coding: utf-8 -*-

from django.db import models

from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookComments'
        db.create_table(u'djangocms_fbcomments_facebookcomments', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('app_id', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('num_posts', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('order_by', self.gf('django.db.models.fields.CharField')(default='social', max_length=20)),
            ('colour_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
            ('load_trigger', self.gf('django.db.models.fields.CharField')(default='immediately', max_length=100)),
            ('button_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'djangocms_fbcomments', ['FacebookComments'])

    def backwards(self, orm):
        # Deleting model 'FacebookComments'
        db.delete_table(u'djangocms_fbcomments_facebookcomments')

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'djangocms_fbcomments.facebookcomments': {
            'Meta': {'object_name': 'FacebookComments', '_ormbases': ['cms.CMSPlugin']},
            'app_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'button_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'colour_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'load_trigger': ('django.db.models.fields.CharField', [], {'default': "'immediately'", 'max_length': '100'}),
            'num_posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'order_by': ('django.db.models.fields.CharField', [], {'default': "'social'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['djangocms_fbcomments']
