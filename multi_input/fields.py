# fields
from django.forms import fields
from django.core.exceptions import ValidationError

from widgets import MobilePhoneWidget

class MobilePhoneField(fields.MultiValueField):
    widget = MobilePhoneWidget()

    def __init__(self, *args, **kwargs):
        fs = (
            fields.CharField(required=True, min_length=4, max_length=4), # ex: '0955'
            fields.CharField(required=True, min_length=3, max_length=3), # ex: '555'
            fields.CharField(required=True, min_length=3, max_length=3), # ex: '710'
        )
        super(MobilePhoneField, self).__init__(fs, *args, **kwargs)

    def compress(self, data_list):
        if data_list and len(data_list) is 3:
            for n in data_list:
                if not n.isdigit():
                    raise ValidationError(u'please enter correct length')        

            if not data_list[0].startswith('09'):
                raise ValidationError(u'please enter correct prefix')        

            return '-'.join(data_list)

        return None
