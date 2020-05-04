from django.urls import path

from . import views

urlpatterns = [
    path('conversations', views.conversations, name='conversations'),
    path('conversation/<str:receiver>', views.user_conversation, name='user_conversation'),
    path('message/<str:conversation>/<str:receiver>/sent', views.message_sent, name='message_sent'),
    path('conversation/<str:pk>/delete', views.conversation_delete, name='conversation_delete'),
]
