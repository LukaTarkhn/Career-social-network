from django.forms import ModelForm

from .models import Organization


class OrganizationAddForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_website']


class OrganizationEditForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['url', 'organization_name', 'organization_phone', 'organization_email', 'organization_alter_names',
                  'organization_logo', 'organization_header_logo', 'organization_about', 'organization_specialization',
                  'organization_website', 'organization_address', 'number_of_employees']

    def save(self, commit=True):
        organization_info = self.instance
        organization_info.url = self.cleaned_data['url']
        organization_info.organization_name = self.cleaned_data['organization_name']
        organization_info.organization_phone = self.cleaned_data['organization_phone']
        organization_info.organization_email = self.cleaned_data['organization_email']
        organization_info.organization_alter_names = self.cleaned_data['organization_alter_names']
        organization_info.organization_about = self.cleaned_data['organization_about']
        organization_info.organization_specialization = self.cleaned_data['organization_specialization']
        organization_info.organization_website = self.cleaned_data['organization_website']
        organization_info.organization_address = self.cleaned_data['organization_address']
        organization_info.number_of_employees = self.cleaned_data['number_of_employees']

        if self.cleaned_data['organization_logo']:
            organization_info.organization_logo = self.cleaned_data['organization_logo']
        if self.cleaned_data['organization_header_logo']:
            organization_info.organization_header_logo = self.cleaned_data['organization_header_logo']

        if commit:
            organization_info.save()
        return organization_info
