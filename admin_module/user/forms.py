from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class CreateUserForm(forms.ModelForm):
    field_order = ('username', 'password', 'phone_number', 'email', 'first_name', 'last_name')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = User
        exclude = ('last_login', 'user_permissions', 'groups', 'country_code', 'date_joined')