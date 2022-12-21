from django import forms
from django.forms.widgets import Textarea


from estate_module.models import Estate


class CreateEstateForm(forms.ModelForm):
    field_order = ('title', 'latitude', 'longitude', 'consultant', 'number_of_rooms',
                    'floor', 'meterage', 'price', 'deposit', 'ad_type', 'build_date',
                    'description', 'address', 'estate_properties', 'category')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Estate
        exclude = ('expire_date', 'images')



class UpdateEstateForm(forms.ModelForm):
    field_order = ('title', 'latitude', 'longitude', 'consultant', 'number_of_rooms',
                    'floor', 'meterage', 'price', 'deposit', 'ad_type', 'build_date',
                    'description', 'address', 'estate_properties', 'category')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Estate
        exclude = ('expire_date', 'images')