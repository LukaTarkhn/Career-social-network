from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account, Specialization, WorkExperience, Education, Language, Contact, MoreEducation
from django.contrib.auth.models import Group


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone', 'living_city', 'gender', 'birth_day',
                    'profile_pic', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    search_fields = ('email', 'username', 'phone', 'first_name', 'last_name', 'living_city', 'gender', 'birth_day')
    list_editable = ('is_active',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)


admin.site.unregister(Group)


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'work_preparedness', 'min_salary', 'qualification', 'sphere', 'skills',
                    'remote_work', 'date_created')
    list_display_links = ('user', 'specialization')
    search_fields = ('user', 'specialization', 'min_salary', 'qualification', 'sphere')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Specialization, SpecializationAdmin)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'position', 'location', 'start_date', 'end_date', 'present', 'responsibilities',
                    'skills', 'date_created')
    list_display_links = ('user', 'name')
    search_fields = ('user', 'name', 'position', 'skills')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(WorkExperience, WorkExperienceAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'faculty', 'degree', 'location', 'start_date', 'end_date', 'present',
                    'specialization', 'date_created')
    list_display_links = ('user', 'name')
    search_fields = ('user', 'name', 'faculty', 'degree')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Education, EducationAdmin)


class MoreEducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'course_name', 'theme', 'start_date', 'end_date', 'present', 'about_course',
                    'date_created')
    list_display_links = ('user', 'name')
    search_fields = ('user', 'name', 'course_name', 'theme')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MoreEducation, MoreEducationAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'level', 'date_created')
    list_display_links = ('user',)
    search_fields = ('user', 'language', 'level')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Language, LanguageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'website', 'facebook', 'github', 'twitter', 'date_created')
    list_display_links = ('user', )
    search_fields = ('user', )
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Contact, ContactAdmin)
