from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect

from .models import Account


class PersonalEditForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name']

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                Account.objects.exclude(username=self.instance.username).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('This link already used')


class PasswordChangeForm(ModelForm):
    class Meta:
        model = Account
        fields = ['password', 'email']

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                Account.objects.exclude(email=self.instance.email).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('This email address already used')


