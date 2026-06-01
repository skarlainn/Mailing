from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import RecipientListView, RecipientDetailsView, RecipientCreateView, RecipientUpdateView, RecipientDeleteView


app_name = MailingConfig.name

urlpatterns = [
    path('', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/<int:pk>/', RecipientDetailsView.as_view(), name='recipient'),
    path("new/", RecipientCreateView.as_view(), name="recipient_create"),
    path("update/<int:pk>/", RecipientUpdateView.as_view(), name="recipient_update"),
    path("delete/<int:pk>/", RecipientDeleteView.as_view(), name="recipient_delete"),
]