import datetime
from django.conf import settings
from django.core.mail import send_mail
from cursach.models import Mailing, MailingTry


def client_mailing(**kwargs):
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
