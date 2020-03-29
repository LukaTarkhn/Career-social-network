from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'living_city', 'gender', 'birth_day', 'profile_pic', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'living_city', 'gender', 'birth_day')
    list_editable = ('is_active',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)


# class AccountMoreAdmin(admin.ModelAdmin):
#     list_display = ('user', 'profile_pic', 'about_me', 'birth_day', 'living_city', 'last_update')
#     list_display_links = ('user', 'profile_pic')
#     search_fields = ('user', 'birth_day', 'living_city')
#     ordering = ('user',)
#     readonly_fields = ()
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# admin.site.register(AccountMore, AccountMoreAdmin)
