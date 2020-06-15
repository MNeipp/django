from django import forms
from django.core.exceptions import ValidationError
from .models import *



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        widgets ={
            'password': forms.PasswordInput
        }
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password',
                "Passwords don't match"
            )
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)