from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.utils.timezone import now

from .forms import ConversationCreateForm, MessageSentForm
from conversations.models import Conversation, Message
from accounts.models import Account


def conversations(request):
    if request.user.is_authenticated:
        conversations_all = Conversation.objects.filter(Q(starter=request.user) |
                                                        Q(receiver=request.user))
        conversation_messages = []
        for conversation in conversations_all:
            conversation_messages.append(Message.objects.filter(conversation_id=conversation.pk).last())

        context = {
            'messages_all': conversation_messages
        }
        return render(request, 'conversations/conversation.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def user_conversation(request, receiver):
    if request.user.is_authenticated:
        receiver_user = Account.objects.filter(username=receiver).first()
        conversation = Conversation.objects.filter(Q(starter=request.user, receiver=receiver_user) |
                                                   Q(starter=receiver_user, receiver=request.user))
        conversation_all = Conversation.objects.filter(Q(starter=request.user) |
                                                       Q(receiver=request.user))
        conversation_messages = []
        for conversation_message in conversation_all:
            conversation_messages.append(Message.objects.filter(conversation_id=conversation_message.pk).last())
        Account.objects.filter(pk=request.user.pk).update(last_login=now())
        if conversation.exists():
            messages_all = Message.objects.filter(conversation=conversation.first()).order_by('date_created')
            if messages_all.exists():
                Message.objects.filter(user=receiver_user, pk=messages_all.last().pk).update(seen_date=now())
                if messages_all.last().date_created < messages_all.last().seen_date:
                    Message.objects.filter(pk=messages_all.last().pk).update(seen=True)

            context = {
                'user_messages': messages_all,
                'receiver_user': receiver_user,
                'this_conversation': conversation.first(),
                'all_conversations': conversation_messages,
                'last_message': messages_all.last(),
            }
            return render(request, 'conversations/conversation.html', context)
        elif request.method == 'POST':
            form = ConversationCreateForm(request.POST or None)
            form2 = MessageSentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.starter = request.user
                obj.receiver = receiver_user
                obj.save()
                obj2 = form2.save(commit=False)
                obj2.conversation = conversation.first()
                obj2.user = request.user
                obj2.message = ''
                obj2.save()
                messages.success(request, 'Conversation created')
                return redirect('user_conversation', receiver_user.username)
        else:
            return redirect('members')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def message_sent(request, conversation, receiver):
    if request.user.is_authenticated:
        form = MessageSentForm(request.POST)
        conversation_info = Conversation.objects.filter(Q(pk=conversation, receiver=request.user) |
                                                        Q(pk=conversation, starter=request.user)).first()
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.conversation = conversation_info
                obj.user = request.user
                obj.message = request.POST['message']
                obj.save()
                messages.success(request, 'Message sent')
                return redirect('user_conversation', receiver)
        context = {
            'form': form
        }
        return render(request, 'conversations/conversation.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def conversation_delete(request, pk):
    if request.user.is_authenticated:
        conversation_for_delete = get_object_or_404(Conversation, pk=pk)
        if request.method == 'POST':
            if conversation_for_delete.starter == request.user:
                Conversation.objects.filter(pk=pk).update(starter_delete=True)
                messages.success(request, 'Conversation successfully deleted')
                if conversation_for_delete.receiver_delete:
                    conversation_for_delete.delete()
                    return redirect('conversations')
                else:
                    return redirect('conversations')
            elif conversation_for_delete.receiver == request.user:
                Conversation.objects.filter(pk=pk).update(receiver_delete=True)
                messages.success(request, 'Conversation successfully deleted')
                if conversation_for_delete.starter_delete:
                    conversation_for_delete.delete()
                    return redirect('conversations')
                else:
                    return redirect('conversations')

        context = {'conversation_for_delete': conversation_for_delete}
        return render(request, 'conversations/conversation.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


