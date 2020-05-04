from django.contrib import admin
from conversations.models import Conversation, Message


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('starter', 'receiver', 'starter_delete', 'receiver_delete', 'date_created')
    list_display_links = ('starter', 'receiver')
    search_fields = ('starter', 'receiver')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Conversation, ConversationAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'user', 'message', 'seen', 'seen_date', 'date_created')
    list_display_links = ('conversation', 'user')
    search_fields = ('conversation', 'user', 'message')
    ordering = ('date_created',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Message, MessageAdmin)
