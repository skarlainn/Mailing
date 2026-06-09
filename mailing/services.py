from django.core.cache import cache
from .models import Recipient, Message, Mailing


def get_all_recipients():
    recipients = cache.get("recipients")
    if recipients is None:
        recipients = Recipient.objects.all()
        cache.set("recipients", recipients, 120)  # кэш на 2 минуты
    return recipients


def get_all_messages():
    messages = cache.get("messages")
    if messages is None:
        messages = Message.objects.all()
        cache.set("messages", messages, 120)
    return messages


def get_all_mailing():
    mailing = cache.get("mailing")
    if mailing is None:
        mailing = Mailing.objects.all()
        cache.set("mailing", mailing, 120)
    return mailing