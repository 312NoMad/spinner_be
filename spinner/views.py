from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Gift, Spin, Wheel, Code
from .serializers import SpinSerializer, WheelSerializer, GiftSerializer, CodeSerializer


class CodeViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = CodeSerializer


class SpinViewSet(ModelViewSet):
    queryset = Spin.objects.all()
    serializer_class = SpinSerializer
    permission_classes = [AllowAny]


class WheelViewSet(ModelViewSet):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer
    permission_classes = [AllowAny]


class GiftViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
