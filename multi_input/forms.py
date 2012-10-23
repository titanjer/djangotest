# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
from django.conf import settings

from fields import MobilePhoneField


class MultiInputForm(forms.Form):

    mobile = MobilePhoneField(required=True, )

    def __init__(self, *args, **kwargs):
        super(MultiInputForm, self).__init__(*args, **kwargs)

