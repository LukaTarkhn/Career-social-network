from django.contrib import admin
from vacancies.models import Vacancy, VacancyResponse


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('organization', 'title', 'url', 'qualification', 'salary', 'location', 'work_type', 'remote_work',
                    'description', 'bonuses', 'instructions', 'sphere', 'skills', 'date_created')
    list_display_links = ('organization', 'title', )
    search_fields = ('title', 'qualification', 'salary', 'remote_work', 'sphere')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Vacancy, VacancyAdmin)


class VacancyResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'vacancy', 'description', 'status', 'date_created')
    list_display_links = ('user', 'vacancy')
    search_fields = ('status', 'date_created', )
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(VacancyResponse, VacancyResponseAdmin)
