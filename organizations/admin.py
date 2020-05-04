from django.contrib import admin
from organizations.models import Organization, OrganizationOwner


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'url', 'organization_phone', 'organization_email',
                    'organization_website', 'organization_website', 'organization_address', 'number_of_employees',
                    'date_created')
    list_display_links = ('organization_name', 'url')
    search_fields = ('organization_name', 'organization_email')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Organization, OrganizationAdmin)


class OrganizationOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'role', 'date_created')
    list_display_links = ('user', 'organization')
    search_fields = ('user', 'organization', 'role')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(OrganizationOwner, OrganizationOwnerAdmin)
