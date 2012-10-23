# widgets
from django.forms import widgets
from django.conf import settings
from django.template.defaulttags import mark_safe


class MobilePhoneWidget(widgets.MultiWidget):

    def __init__(self, attrs=None):
        self.attrs = attrs or {}
        ws = (
                widgets.TextInput(attrs=self.attrs),
                widgets.TextInput(attrs=self.attrs),
                widgets.TextInput(attrs=self.attrs),
        )
        super(MobilePhoneWidget, self).__init__(ws, attrs)

    def decompress(self, value):
        if value:
            nums = value.split('-')
            if len(nums) is 3:
                return nums
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)


