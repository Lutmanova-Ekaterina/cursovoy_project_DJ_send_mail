from django.urls import path

from cursach.apps import CursachConfig
from cursach.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, MailingDetailView, LetterListView, LetterCreateView, LetterUpdateView, LetterDeleteView, LetterDetailView, mailing_client, stats


app_name = CursachConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='cursach'),
    path('client_create/', ClientCreateView.as_view(), name='create_client'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client_datail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('mailing/', MailingListView.as_view(), name='mailing'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('letter/', LetterListView.as_view(), name='letter'),
    path('letter_create/', LetterCreateView.as_view(), name='letter_create'),
    path('letter_update/<int:pk>/', LetterUpdateView.as_view(), name='letter_update'),
    path('letter_delete/<int:pk>/', LetterDeleteView.as_view(), name='letter_delete'),
    path('letter_detail/<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('mailing_client/', mailing_client, name='status'),
    path('status/', stats, name='stats')
]


