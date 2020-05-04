from django import forms
from django.forms import ModelForm

from .models import Account, Specialization, Contact, WorkExperience, Education, MoreEducation, Language


class PersonalEditForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'profile_pic', 'phone', 'about_me', 'birth_day', 'living_city', 'gender',
                  'website']

    def save(self, commit=True):
        personal_info = self.instance
        personal_info.first_name = self.cleaned_data['first_name']
        personal_info.last_name = self.cleaned_data['last_name']
        personal_info.phone = self.cleaned_data['phone']
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


class SpecializationAddForm(ModelForm):
    class Meta:
        model = Specialization
        fields = []


class SpecializationEditForm(ModelForm):
    class Meta:
        model = Specialization
        fields = ['work_preparedness', 'min_salary', 'specialization', 'qualification', 'sphere', 'skills',
                  'remote_work']

    def save(self, commit=True):
        specialization_info = self.instance
        specialization_info.work_preparedness = self.cleaned_data['work_preparedness']
        specialization_info.min_salary = self.cleaned_data['min_salary']
        specialization_info.specialization = self.cleaned_data['specialization']
        specialization_info.qualification = self.cleaned_data['qualification']
        specialization_info.sphere = self.cleaned_data['sphere']
        specialization_info.skills = self.cleaned_data['skills']
        specialization_info.remote_work = self.cleaned_data['remote_work']

        if commit:
            specialization_info.save()
        return specialization_info


class ContactAddForm(ModelForm):
    class Meta:
        model = Contact
        fields = []


class ContactEditForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['phone', 'email', 'website', 'facebook', 'github', 'twitter']

    def save(self, commit=True):
        contact_info = self.instance
        contact_info.phone = self.cleaned_data['phone']
        contact_info.email = self.cleaned_data['email']
        contact_info.website = self.cleaned_data['website']
        contact_info.facebook = self.cleaned_data['facebook']
        contact_info.github = self.cleaned_data['github']
        contact_info.twitter = self.cleaned_data['twitter']

        if commit:
            contact_info.save()
        return contact_info


class WorkExperienceAddForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['name', 'position', 'location', 'start_date', 'end_date', 'present', 'responsibilities', 'skills']


class WorkExperienceEditForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['name', 'position', 'location', 'start_date', 'end_date', 'present', 'responsibilities', 'skills']

    def save(self, commit=True):
        experience_info = self.instance
        experience_info.name = self.cleaned_data['name']
        experience_info.position = self.cleaned_data['position']
        experience_info.location = self.cleaned_data['location']
        experience_info.start_date = self.cleaned_data['start_date']
        experience_info.end_date = self.cleaned_data['end_date']
        experience_info.present = self.cleaned_data['present']
        experience_info.responsibilities = self.cleaned_data['responsibilities']
        experience_info.skills = self.cleaned_data['skills']

        if commit:
            experience_info.save()
        return experience_info


class EducationAddForm(ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'faculty', 'degree', 'location', 'start_date', 'end_date', 'present', 'specialization']


class EducationEditForm(ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'faculty', 'degree', 'location', 'start_date', 'end_date', 'present', 'specialization']

    def save(self, commit=True):
        education_info = self.instance
        education_info.name = self.cleaned_data['name']
        education_info.faculty = self.cleaned_data['faculty']
        education_info.degree = self.cleaned_data['degree']
        education_info.location = self.cleaned_data['location']
        education_info.start_date = self.cleaned_data['start_date']
        education_info.end_date = self.cleaned_data['end_date']
        education_info.present = self.cleaned_data['present']
        education_info.specialization = self.cleaned_data['specialization']

        if commit:
            education_info.save()
        return education_info


class MoreEducationAddForm(ModelForm):
    class Meta:
        model = MoreEducation
        fields = ['name', 'course_name', 'theme', 'start_date', 'end_date', 'present', 'about_course']


class MoreEducationEditForm(ModelForm):
    class Meta:
        model = MoreEducation
        fields = ['name', 'course_name', 'theme', 'start_date', 'end_date', 'present', 'about_course']

    def save(self, commit=True):
        more_education_info = self.instance
        more_education_info.name = self.cleaned_data['name']
        more_education_info.course_name = self.cleaned_data['course_name']
        more_education_info.theme = self.cleaned_data['theme']
        more_education_info.start_date = self.cleaned_data['start_date']
        more_education_info.end_date = self.cleaned_data['end_date']
        more_education_info.present = self.cleaned_data['present']
        more_education_info.about_course = self.cleaned_data['about_course']

        if commit:
            more_education_info.save()
        return more_education_info


class LanguageAddForm(ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'level']


class LanguageEditForm(ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'level']

    def save(self, commit=True):
        language_info = self.instance
        language_info.language = self.cleaned_data['language']
        language_info.level = self.cleaned_data['level']

        if commit:
            language_info.save()
        return language_info
