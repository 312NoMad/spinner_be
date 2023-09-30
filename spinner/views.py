from rest_framework.viewsets import ModelViewSet

from .models import Gift, Spin, Wheel, Code
from .serializers import SpinSerializer, WheelSerializer, GiftSerializer, CodeSerializer


class CodeViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = CodeSerializer


class SpinViewSet(ModelViewSet):
    queryset = Spin.objects.all()
    serializer_class = SpinSerializer


class WheelViewSet(ModelViewSet):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer


class CodeViewSet(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class GiftViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
