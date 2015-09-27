# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import get_language, to_locale

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .models import FacebookComments


class FacebookCommentsPlugin(CMSPluginBase):
    module = settings.DJANGOCMS_FBCOMMENTS_PLUGIN_MODULE
    name = settings.DJANGOCMS_FBCOMMENTS_PLUGIN_NAME
    model = FacebookComments
    render_template = settings.DJANGOCMS_FBCOMMENTS_PLUGIN_TEMPLATE

    def render(self, context, instance, placeholder):
        context = super(FacebookCommentsPlugin, self).render(context, instance, placeholder)
        request = context.get('request')

        context['language_code'] = to_locale(get_language())
        context['page_url'] = request.build_absolute_uri(location=request.path_info)
        return context


plugin_pool.register_plugin(FacebookCommentsPlugin)
