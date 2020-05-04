from django.forms import ModelForm
from .models import Conversation, Message


class ConversationCreateForm(ModelForm):
    class Meta:
        model = Conversation
        fields = []


class MessageSentForm(ModelForm):
    class Meta:
        model = Message
        fields = []