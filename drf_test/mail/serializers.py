from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from .models import Letters, Packages


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = '__all__'


# class PackagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Packages
#         fields = '__all__'

class PackagesSerializer(serializers.Serializer):
    PACKAGE_TYPES = (
        (1, 'Мелкий пакет'),
        (2, 'Посылка'),
        (3, 'Посылка 1 класса'),
        (4, 'Ценная посылка'),
        (5, 'Посылка международная'),
        (6, 'Экспресс-посылка'),
    )
    id = serializers.IntegerField(read_only=True)
    sender_name = serializers.CharField(max_length=50)
    recipient_name = serializers.CharField(max_length=50)
    departure_name = serializers.CharField(max_length=250)
    arrival_name = serializers.CharField(max_length=250)
    departure_index = serializers.IntegerField(validators=[
        MaxValueValidator(999999),
        MinValueValidator(100000)
    ])
    arrival_index = serializers.IntegerField(validators=[
        MaxValueValidator(999999),
        MinValueValidator(100000)
    ])
    phone = serializers.CharField(max_length=12)
    package_type = serializers.ChoiceField(choices=PACKAGE_TYPES, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ])
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def create(self, validated_data):
        return Packages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sender_name = validated_data.get("sender_name", instance.sender_name)
        instance.recipient_name = validated_data.get("recipient_name", instance.recipient_name)
        instance.departure_name = validated_data.get("departure_name", instance.departure_name)
        instance.arrival_name = validated_data.get("arrival_name", instance.arrival_name)
        instance.departure_index = validated_data.get("departure_index", instance.departure_index)
        instance.arrival_index = validated_data.get("arrival_index", instance.arrival_index)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.package_type = validated_data.get("package_type", instance.package_type)
        instance.amount = validated_data.get("amount", instance.amount)

        instance.save()
        return instance
