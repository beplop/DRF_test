from django.db import models

class Letters(models.Model):
    """Письма"""
    sender_name = models.CharField('ФИО отправителя', max_length=50, null=False)
    recipent_name = models.CharField('ФИО получателя', max_length=50, null=False)
    departure_name = models.CharField('пункт отправки', max_length=250, null=False)
    arrival_name = models.CharField('пункт получения', max_length=250, null=False)
    departure_index = models.IntegerField('индекс места отправки', null=False)
    arrival_index = models.IntegerField('индекс места получения', null=False)
    letter_type = models.IntegerField('тип письма', null=False)
    letter_weight = models.IntegerField('вес письма', null=False)

    def __str__(self):
        return self.sender_name

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

class Packages(models.Model):
    """Посылки"""
    sender_name = models.CharField('ФИО отправителя', max_length=50, null=False)
    recipent_name = models.CharField('ФИО получателя', max_length=50, null=False)
    departure_name = models.CharField('пункт отправки', max_length=250, null=False)
    arrival_name = models.CharField('пункт получения', max_length=250, null=False)
    departure_index = models.IntegerField('индекс места отправки', null=False)
    arrival_index = models.IntegerField('индекс места получения', null=False)
    phone = models.CharField('телефон для извещения', max_length=20, null=False)
    package_type = models.IntegerField('тип посылки', null=False)
    amount = models.IntegerField('сумма платежа', null=False)

    def __str__(self):
        return self.sender_name

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
