# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from .conf import settings


@python_2_unicode_compatible
class FacebookComments(CMSPlugin):
    app_id = models.CharField(
        _('Facebook App ID'), max_length=100,
        default=settings.DJANGOCMS_FBCOMMENTS_APP_ID)
    title = models.CharField(_('Title'), max_length=255, blank=True)
    num_posts = models.PositiveIntegerField(
        _('Number of Comments'), default=10,
        help_text=_('The number of comments to show by default.'))
    order_by = models.CharField(
        _('Comments Ordering'), max_length=20,
        choices=settings.DJANGOCMS_FBCOMMENTS_COMMENTS_ORDERING,
        default=settings.DJANGOCMS_FBCOMMENTS_COMMENTS_ORDERING[0][0],
        help_text=_('The order to use when displaying comments.'))
    colour_scheme = models.CharField(
        _('Colour Scheme'), max_length=50,
        choices=settings.DJANGOCMS_FBCOMMENTS_COLOUR_SCHEMES,
        default=settings.DJANGOCMS_FBCOMMENTS_COLOUR_SCHEMES[0][0]
    )

    load_trigger = models.CharField(
        _('How to load comments'), max_length=100,
        default=settings.DJANGOCMS_FBCOMMENTS_LOADING_CHOICES[0][0],
        choices=settings.DJANGOCMS_FBCOMMENTS_LOADING_CHOICES)

    button_text = models.CharField(
        _('Button Text'), max_length=100, blank=True,
        help_text=_('By default it will be "Load Comments..."'))

    def __str__(self):
        return u'%s' % _('Facebook Comments')
