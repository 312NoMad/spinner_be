from rest_framework.serializers import ModelSerializer

from .models import Gift, Spin, Wheel, Code


class GiftSerializer(ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'


class WheelSerializer(ModelSerializer):
    gifts = GiftSerializer(many=True)

    class Meta:
        model = Wheel
        fields = '__all__'


class SpinSerializer(ModelSerializer):
    wheel = WheelSerializer()
    prize = GiftSerializer()

    class Meta:
        model = Spin
        fields = '__all__'


class CodeSerializer(ModelSerializer):
    wheel = WheelSerializer()

    class Meta:
        model = Code
        fields = '__all__'
