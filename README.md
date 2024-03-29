# Курсовой проект по web-разработке на Django

## **Контекст**

<aside>
📍 Для удержания текущих клиентов зачастую используются вспомогательные или "прогревающие" рассылки для информирования и привлечения.

Вам нужно разработать **сервис управления рассылками, администрирования и получения статистики**.

</aside>

### Описание задач

- Реализуйте интерфейс заполнения рассылок, то есть CRUD механизм для управления рассылками.
- Реализуйте скрипт рассылки, который работает как из командой строки, так и по расписанию.
- Добавьте настройки конфигурации для периодического запуска задачи.

### Сущности системы

- Клиент сервиса:
    - контактный email
    - фио
    - комментарий
- Рассылка (настройки)
    - время рассылки
    - периодичность: раз в день, раз в неделю, раз в месяц
    - статус рассылки (завершена, создана, запущена)
- Сообщение для рассылки
    - тема письма
    - тело письма
- Попытка рассылки
    - дата и время последней попытки
    - статус попытки
    - ответ почтового сервера, если он был

<aside>
ℹ️ **Примечание:**
Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей, либо добавлять вспомогательные модели.

</aside>

### Логика работы системы

- После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
- Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
- По ходу отправки сообщений должна собираться статистика (см. описание сущности "сообщение" и "попытка" выше) по каждому сообщению для последующего формирования отчётов.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

<aside>
👨🏻‍💻 **Рекомендации**

- реализовать интерфейс можно с помощью uikit Bootstrap
- для работы с периодическими задачами можно использовать либо crontab задачи в чистом виде, либо изучить дополнительно библиотеку https://pypi.org/project/django-crontab/
</aside>

### Критерии приемки

- [ ]  Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя
- [ ]  Реализована вся требуемая логика поведения
- [ ]  Интерфейс понятен и соответствует базовым требованиям системы
- [ ]  Решение выложено на [github.com](http://github.com/)
