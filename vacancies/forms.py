from django.forms import ModelForm

from .models import Vacancy, VacancyResponse


class VacancyAddForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'qualification', 'salary', 'location', 'work_type', 'remote_work', 'description', 'bonuses',
                  'instructions', 'sphere', 'skills']


class VacancyEditForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'qualification', 'salary', 'location', 'work_type', 'remote_work', 'description', 'bonuses',
                  'instructions', 'sphere', 'skills']

    def save(self, commit=True):
        vacancy_info = self.instance
        vacancy_info.title = self.cleaned_data['title']
        vacancy_info.qualification = self.cleaned_data['qualification']
        vacancy_info.salary = self.cleaned_data['salary']
        vacancy_info.location = self.cleaned_data['location']
        vacancy_info.work_type = self.cleaned_data['work_type']
        vacancy_info.remote_work = self.cleaned_data['remote_work']
        vacancy_info.description = self.cleaned_data['description']
        vacancy_info.bonuses = self.cleaned_data['bonuses']
        vacancy_info.instructions = self.cleaned_data['instructions']
        vacancy_info.sphere = self.cleaned_data['sphere']
        vacancy_info.skills = self.cleaned_data['skills']

        if commit:
            vacancy_info.save()
        return vacancy_info


class ResponseAddForm(ModelForm):
    class Meta:
        model = VacancyResponse
        fields = ['description']


class ResponseEditForm(ModelForm):
    class Meta:
        model = VacancyResponse
        fields = ['status']

    def save(self, commit=True):
        response_info = self.instance
        response_info.status = self.cleaned_data['status']

        if commit:
            response_info.save()
        return response_info
