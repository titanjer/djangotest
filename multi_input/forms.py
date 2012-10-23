# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
from django.conf import settings

from fields import MobilePhoneField
from widgets import MobilePhoneWidget


class MultiInputForm(forms.Form):

    mobile = MobilePhoneField(required=True, widget=MobilePhoneWidget())

    #class Media:
    #    css = {'all': ('css/form.css',)}
    #    js = ('js/form/customer.js', )

    def __init__(self, *args, **kwargs):
        super(MultiInputForm, self).__init__(*args, **kwargs)

