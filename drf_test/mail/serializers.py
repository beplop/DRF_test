from rest_framework import serializers
from .models import Letters, Packages


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = '__all__'


class PackagesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender_name = serializers.CharField(max_length=50)
    recipent_name = serializers.CharField(max_length=50)
    departure_name = serializers.CharField(max_length=250)
    arrival_name = serializers.CharField(max_length=250)
    departure_index = serializers.IntegerField()
    arrival_index = serializers.IntegerField()
    phone = serializers.CharField(max_length=20)
    package_type = serializers.IntegerField()
    amount = serializers.IntegerField()

    def create(self, validated_data):
        return Packages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sender_name = validated_data.get("sender_name", instance.sender_name)
        instance.recipent_name = validated_data.get("recipent_name", instance.recipent_name)
        instance.departure_name = validated_data.get("departure_name", instance.departure_name)
        instance.arrival_name = validated_data.get("arrival_name", instance.arrival_name)
        instance.departure_index = validated_data.get("departure_index", instance.departure_index)
        instance.arrival_index = validated_data.get("arrival_index", instance.arrival_index)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.package_type = validated_data.get("package_type", instance.package_type)
        instance.amount = validated_data.get("amount", instance.amount)

        instance.save()
        return instance
