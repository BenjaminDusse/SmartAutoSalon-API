from rest_framework import serializers
from .models import User, Order, CarModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'lastname', 'father_name', 'phone_number', 'passport']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

    def to_representation(self, instance):
        return {
            "data": {
                'user_name': instance.user.name,
                'car_model': instance.car_model.name,
                'car_name': instance.name,
                'type': instance.type,
                'position': instance.position,
                'production': instance.production,
                'year': instance.year,
                'color': instance.color,
                'Additional': instance.Additional
            }
        }
