from django.db import models

class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите электронную почту")
    full_name = models.CharField(max_length=150, verbose_name="ФИО", help_text="Введите ФИО")
    comment = models.TextField(verbose_name="Комментарий", help_text="Напишите комментарий", blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
        ordering = ["email"]


class Message(models.Model):
    topic = models.CharField(max_length=150, verbose_name="Тема сообщения", help_text="Введите тему сообщения")
    text = models.TextField(verbose_name="Текст сообщения", help_text="Напишите сообщение")

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]


class Mailing(models.Model):
    first_sending = models.DateTimeField(verbose_name="Дата первой рассылки", auto_now_add=True)
    end_sending = models.DateTimeField(verbose_name="Дата окончания рассылки",
                                       help_text="Введите дату окончания рассылки", blank=True, null=True)

    STATUS_OF_MAILING = [
        ("created", "Создана"),
        ("launched", "Запущена"),
        ("completed", "Завершена"),
    ]
    status = models.CharField(choices=STATUS_OF_MAILING, default='created', verbose_name="Статус рассылки",
                              help_text="Выберите статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение",
                                help_text="Выберите сообщение")
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели", help_text="Выберите получателей")

    def __str__(self):
        return f"Рассылка №{self.pk}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["status"]


class AttemptSending(models.Model):
    time = models.DateTimeField(verbose_name="Дата и время попытки", auto_now=True)

    STATUS_OF_ATTEMPT = [
        ('success', 'Успешно'),
        ('not_success', 'Не успешно'),
    ]
    status = models.CharField(choices=STATUS_OF_ATTEMPT, default='not_success', verbose_name="Статус попытки")
    response = models.TextField(verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")

    def __str__(self):
        return f'Попытка №{self.pk}'

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["time"]
