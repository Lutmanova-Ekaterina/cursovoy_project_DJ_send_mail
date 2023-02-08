from datetime import datetime, date
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=250, verbose_name='Контактная почта')
    full_name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.full_name}, {self.email}, {self.comment}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    ONE_DAY = 'one_day'
    ONE_WEEK = 'one_week'
    ONE_MONTH = 'one_month'
    PERIODS = (
        ('one_day', 'раз в день'),
        ('one_week', "раз в неделю"),
        ('one_month', "раз в месяц")
    )
    STATUS_COMPLETED = 'completed'
    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'
    STATUSES = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена')
    )

    client = models.ForeignKey('cursach.Client', verbose_name='Клиент', on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey('cursach.Letter', verbose_name='Сообщение', on_delete=models.SET_NULL, null=True)
    time_of_mailing = models.DateTimeField(verbose_name='Время рассылки', **NULLABLE)
    periodicity = models.CharField(choices=PERIODS, default=ONE_WEEK, max_length=50,
                                   verbose_name='Периодичность')
    mailing_status = models.CharField(choices=STATUSES, default=STATUS_COMPLETED, max_length=50,
                                      verbose_name='Статус рассылки')
    start_date = models.DateTimeField(default=date.today, verbose_name='Начальная дата')
    end_date = models.DateTimeField(default=date.today, verbose_name='Конечная дата')

    def __str__(self):
        return f'{self.message}, {self.time_of_mailing}, {self.periodicity}, {self.mailing_status}, {self.start_date}, {self.end_date}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Letter(models.Model):
    letter_topic = models.CharField(max_length=350, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Содержимое письма')

    def __str__(self):
        return f'{self.letter_topic}, {self.letter_body}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingTry(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время попытки')
    status = models.CharField(max_length=50, verbose_name='статус попытки')
    answer = models.CharField(max_length=250, verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return f'{self.date}, {self.status}, {self.answer}'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'

