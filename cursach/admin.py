from django.contrib import admin

from cursach.models import Client, Mailing, MailingTry, Letter


@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')


@admin.register(Mailing)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('time_of_mailing', 'periodicity', 'mailing_status', 'start_date', 'end_date')


@admin.register(MailingTry)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'answer')


@admin.register(Letter)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('letter_topic', 'letter_body')
