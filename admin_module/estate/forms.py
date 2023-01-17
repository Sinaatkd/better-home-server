from django import forms
from django.forms.widgets import Textarea


from estate_module.models import Estate, EstateProperty, EstateRegion, EstateImage


class CreateEstateForm(forms.ModelForm):
    field_order = ('title', 'latitude', 'longitude', 'consultant', 'number_of_rooms',
                    'floor', 'meterage', 'price', 'deposit', 'ad_type', 'build_date',
                    'category', 'description', 'address', 'estate_properties')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Estate
        exclude = ('expire_date', 'images', 'fav_of_users')

class UpdateEstateForm(forms.ModelForm):
    field_order = ('title', 'latitude', 'longitude', 'consultant', 'number_of_rooms',
                    'floor', 'meterage', 'price', 'deposit', 'ad_type', 'build_date',
                    'category', 'description', 'address', 'estate_properties')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Estate
        exclude = ('expire_date', 'images', 'fav_of_users')


class CreateEstatePropertyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EstateProperty
        exclude = ('is_active', 'is_delete')



class UpdateEstatePropertyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EstateProperty
        exclude = ('is_active', 'is_delete')



class CreateUpdateEstateRegionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EstateRegion
        exclude = ('is_active', 'is_delete')



class CreateUpdateEstateImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, Textarea) or self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = EstateImage
        exclude = ('is_active', 'is_delete')

