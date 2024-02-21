from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Mail(models.Model):
    """Абстрактная модель почты, содержащая общий набор данных"""
    sender_name = models.CharField('ФИО отправителя', max_length=50)
    recipient_name = models.CharField('ФИО получателя', max_length=50)
    departure_name = models.CharField('пункт отправки', max_length=250)
    arrival_name = models.CharField('пункт получения', max_length=250)
    departure_index = models.PositiveIntegerField('индекс места отправки', validators=[
        MaxValueValidator(999999),
        MinValueValidator(100000)
    ])
    arrival_index = models.PositiveIntegerField('индекс места получения', validators=[
        MaxValueValidator(999999),
        MinValueValidator(100000)
    ])

    class Meta:
        abstract = True


class Letters(Mail):
    """Письма"""
    LETTER_TYPES = (
        (1, 'Письмо'),
        (2, 'Заказное письмо'),
        (3, 'Ценное письмо'),
        (4, 'Экспресс-письмо'),
    )

    letter_type = models.IntegerField('тип письма', choices=LETTER_TYPES, validators=[
        MaxValueValidator(4),
        MinValueValidator(1)
    ])
    letter_weight = models.PositiveSmallIntegerField('вес письма', validators=[
        MaxValueValidator(5000),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.sender_name

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Packages(Mail):
    """Посылки"""
    PACKAGE_TYPES = (
        (1, 'Мелкий пакет'),
        (2, 'Посылка'),
        (3, 'Посылка 1 класса'),
        (4, 'Ценная посылка'),
        (5, 'Посылка международная'),
        (6, 'Экспресс-посылка'),
    )

    phone = models.CharField('телефон для извещения', max_length=12)
    package_type = models.PositiveSmallIntegerField('тип посылки', choices=PACKAGE_TYPES, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ])
    amount = models.DecimalField('сумма платежа', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.sender_name

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
