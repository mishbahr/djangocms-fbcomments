# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from djangocms_fbcomments.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookComments',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('app_id', models.CharField(default=settings.DJANGOCMS_FBCOMMENTS_APP_ID, max_length=100, verbose_name='Facebook App ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('num_posts', models.PositiveIntegerField(default=10, help_text='The number of comments to show by default.', verbose_name='Number of Comments')),
                ('order_by', models.CharField(default=settings.DJANGOCMS_FBCOMMENTS_COMMENTS_ORDERING[0][0], help_text='The order to use when displaying comments.', max_length=20, verbose_name='Comments Ordering', choices=settings.DJANGOCMS_FBCOMMENTS_COMMENTS_ORDERING)),
                ('colour_scheme', models.CharField(default=settings.DJANGOCMS_FBCOMMENTS_COLOUR_SCHEMES[0][0], max_length=50, verbose_name='Colour Scheme', choices=settings.DJANGOCMS_FBCOMMENTS_COLOUR_SCHEMES)),
                ('load_trigger', models.CharField(default=settings.DJANGOCMS_FBCOMMENTS_LOADING_CHOICES[0][0], max_length=100, verbose_name='How to load comments', choices=settings.DJANGOCMS_FBCOMMENTS_LOADING_CHOICES)),
                ('button_text', models.CharField(help_text='By default it will be "Load Comments..."', max_length=100, verbose_name='Button Text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
