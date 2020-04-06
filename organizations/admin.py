from django.contrib import admin
from organizations.models import Organization


class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'organization_name', 'organization_phone', 'organization_email',
                    'organization_website', 'organization_website', 'organization_address', 'number_of_employees',
                    'date_created')
    list_display_links = ('user', 'url', 'organization_name')
    search_fields = ('user', 'organization_name', 'organization_email')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Organization, OrganizationsAdmin)
