from django.db import models
from django.conf import settings


class Conversation(models.Model):
    starter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                verbose_name='Conversation starter', related_name="Conversation_starter")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                 verbose_name='Conversation receiver', related_name="Conversation_receiver")
    starter_delete = models.BooleanField(verbose_name='Starter delete', default=False)
    receiver_delete = models.BooleanField(verbose_name='Receiver delete', default=False)
    date_created = models.DateTimeField(verbose_name='Create date', auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True, verbose_name='Conversation')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='User')
    message = models.TextField(verbose_name='Message', max_length=600, null=True)
    seen = models.BooleanField(verbose_name='Seen', default=False)
    seen_date = models.DateTimeField(verbose_name='Seen date', auto_now_add=True)
    date_created = models.DateTimeField(verbose_name='Create date', auto_now_add=True)

    def __str__(self):
        return str(self.user)
