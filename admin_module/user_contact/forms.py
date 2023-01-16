from django import forms

from user_contact_module.models import UserContact



class CreateUserContactForm(forms.ModelForm):
    field_order = ('customer_phone_number', 'status')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = UserContact
        exclude = ('is_active', 'is_delete', 'consultant')
