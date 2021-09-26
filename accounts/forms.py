from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class FormPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(label='Old password',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':'Enter your old password',
        }))
    new_password1 = forms.CharField(label='New password',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your new password',
        }))
    new_password2 = forms.CharField(label='comfirm password',widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password',
        })) 