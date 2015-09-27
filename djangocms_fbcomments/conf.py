# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class DjangoCMSfbcommentsConf(AppConf):
    PLUGIN_MODULE = _('Generic')
    PLUGIN_NAME = _('Facebook Comments')
    PLUGIN_TEMPLATE = 'djangocms_fbcomments/default.html'

    COMMENTS_ORDERING = (
        ('social', _('Social ranking')),
        ('time', _('Chronological')),
        ('reverse_time', _('Reverse Chronological')),
    )

    COLOUR_SCHEMES = (
        ('light', _('Light')),
        ('dark', _('Dark')),
    )

    LOADING_CHOICES = (
        ('immediately', _('Immediately')),
        ('lazyload', _('Lazy Load')),
        ('click', _('On Click')),
    )

    APP_ID = ''

    class Meta:
        prefix = 'djangocms_fbcomments'
