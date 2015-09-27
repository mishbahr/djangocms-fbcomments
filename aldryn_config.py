# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from aldryn_client import forms


class Form(forms.BaseForm):
    plugin_module = forms.CharField('Plugin module name', initial='Generic')
    plugin_name = forms.CharField('Plugin name', initial='Facebook Comments')
    plugin_template = forms.CharField('Plugin Template', initial='djangocms_fbcomments/default.html')
    app_id = forms.CharField('Facebook App ID', required=False)

    def to_settings(self, data, settings):
        settings['DJANGOCMS_FBCOMMENTS_PLUGIN_MODULE'] = data['plugin_module']
        settings['DJANGOCMS_FBCOMMENTS_PLUGIN_NAME'] = data['plugin_name']
        settings['DJANGOCMS_FBCOMMENTS_PLUGIN_TEMPLATE'] = data['plugin_template']
        settings['DJANGOCMS_FBCOMMENTS_APP_ID'] = data['app_id']
        return settings

