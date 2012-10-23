# fields
from django.forms import fields
from django.core.exceptions import ValidationError

class MobilePhoneField(fields.MultiValueField):

    def __init__(self, *args, **kwargs):
        fs = (
            fields.CharField(required=True, min_length=4, max_length=4),
            fields.CharField(required=True, min_length=3, max_length=3),
            fields.CharField(required=True, min_length=3, max_length=3),
        )
        super(MobilePhoneField, self).__init__(fs, *args, **kwargs)

    def compress(self, data_list):
        if data_list and len(data_list) is 3:
            for n in data_list:
                if not n.isdigit():
                    raise ValidationError(u'please enter correct number')        
            return '-'.join(data_list)
        return None
