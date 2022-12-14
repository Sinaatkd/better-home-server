from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class CreateUserForm(forms.ModelForm):
    field_order = ('username', 'password', 'phone_number', 'email', 'first_name', 'last_name',
                    'ad_monthly_quota','ladder_monthly_quota','special_ad_monthly_quota')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = User
        exclude = ('last_login', 'user_permissions', 'groups', 'country_code', 'date_joined')



class UpdateUserForm(forms.ModelForm):
    field_order = ('username', 'phone_number', 'email', 'first_name', 'last_name',
                    'ad_monthly_quota','ladder_monthly_quota','special_ad_monthly_quota')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type != 'checkbox':
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = User
        exclude = ('last_login', 'user_permissions', 'groups', 'country_code', 'date_joined', 'password')

    
class ChangeUserPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(label='تکرار رمز عبور')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'value': ''})
        
    field_order = ('password', 'confirm_password')

    class Meta:
        model = User
        fields = ('password', 'confirm_password')
    
    def clean(self):
        super(ChangeUserPasswordForm, self).clean()

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self._errors['confirm_password'] = self.error_class(['رمز عبور های وارد شده با یک دیگر مغایرت دارد'])
            
        return self.cleaned_data