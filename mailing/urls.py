from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import RecipientListView, RecipientDetailsView, RecipientCreateView, RecipientUpdateView, RecipientDeleteView, MessageDetailsView, MessageCreateView, MessageUpdateView, MessageDeleteView, MessageListView, MailingSendView


app_name = MailingConfig.name

urlpatterns = [
    path('a/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/<int:pk>/', RecipientDetailsView.as_view(), name='recipient'),
    path("new/recipient/", RecipientCreateView.as_view(), name="recipient_create"),
    path("update/recipient/<int:pk>/", RecipientUpdateView.as_view(), name="recipient_update"),
    path("delete/recipient/<int:pk>/", RecipientDeleteView.as_view(), name="recipient_delete"),
    path('', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailsView.as_view(), name='message'),
    path("new/message/", MessageCreateView.as_view(), name="message_create"),
    path("update/message/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("delete/message/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
    path("mailing_send/<int:pk>/", MailingSendView.as_view(), name="mailing_send"),
]