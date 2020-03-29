from django import forms
from django.forms import ModelForm

from .models import Account


class PersonalEditForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'profile_pic', 'about_me', 'birth_day', 'living_city', 'gender', 'website']

    def save(self, commit=True):
        personal_info = self.instance
        personal_info.first_name = self.cleaned_data['first_name']
        personal_info.last_name = self.cleaned_data['last_name']
        personal_info.about_me = self.cleaned_data['about_me']
        personal_info.birth_day = self.cleaned_data['birth_day']
        personal_info.living_city = self.cleaned_data['living_city']
        personal_info.gender = self.cleaned_data['gender']
        personal_info.website = self.cleaned_data['website']

        if self.cleaned_data['profile_pic']:
            personal_info.profile_pic = self.cleaned_data['profile_pic']

        if commit:
            personal_info.save()
        return personal_info


class EmailUrlEditForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'username']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Account.objects.exclude(username=self.instance.username).get(username=username)
        except Account.DoesNotExist:
            return username.lower()
        raise forms.ValidationError('This link already used')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                Account.objects.exclude(email=self.instance.email).get(email=email)
            except Account.DoesNotExist:
                return email.lower()
            raise forms.ValidationError('This email address already used')

# class PersonalMoreEditForm(ModelForm):
#     class Meta:
#         model = AccountMore
#         fields = ['profile_pic', 'about_me', 'birth_day', 'living_city']
#
#     def save(self, commit=True):
#         personal_info = self.instance
#         personal_info.about_me = self.changed_data['about_me']
#         personal_info.birth_day = self.changed_data['birth_day']
#         personal_info.living_city = self.changed_data['living_city']
#
#         if self.cleaned_data['profile_pic']:
#             personal_info.profile_pic = self.changed_data['profile_pic']
#         if commit:
#             personal_info.save()
#         return personal_info
