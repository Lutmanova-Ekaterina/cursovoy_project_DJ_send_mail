import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from cursach.models import MailingTry, Client, Mailing, Letter


def stats(request):
    context = {
        'object_list': MailingTry.objects.all()
    }
    return render(request, 'cursach/stats.html', context)


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('cursach:cursach')


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('cursach:cursach')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('cursach:cursach')


class ClientDetailView(DeleteView):
    model = Client


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('cursach:mailing')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('cursach:mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('cursach:mailing')


class MailingDetailView(DetailView):
    model = Mailing


class LetterListView(ListView):
    model = Letter


class LetterCreateView(CreateView):
    model = Letter
    fields = '__all__'
    success_url = reverse_lazy('cursach:letter')


class LetterUpdateView(UpdateView):
    model = Letter
    fields = '__all__'
    success_url = reverse_lazy('cursach:letter')


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('cursach:letter')


class LetterDetailView(DetailView):
    model = Letter


def mailing_client(request):
    mailing_items = Mailing.objects.all()
    for item in mailing_items:
        if (
                item.mailing_status == Mailing.STATUS_CREATED or item.mailing_status == Mailing.STATUS_LAUNCHED) and item.start_date == datetime.date.today() and item.end_date >= datetime.date.today() and item.time_of_mailing >= datetime.datetime.now().time():
            item.mailing_status = Mailing.STATUS_LAUNCHED
            item.save()
            try:
                result = send_mail(
                    subject=item.message.letter_topic,
                    message=item.message.letter_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[item.client.email],
                    fail_silently=False
                )
                if result:
                    item.mailing_status = Mailing.STATUS_COMPLETED
                    item.save()
                MailingTry.objects.create(
                    status=item.mailing_status,
                    answer=200
                )
            except Exception as e:
                MailingTry.objects.create(
                    status=item.mailing_status,
                    answer=e
                )
    return redirect(reverse('cursach:mailing'))
