from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import CodeViewSet, SpinViewSet, WheelViewSet, GiftViewSet

router = DefaultRouter()
router.register('code', CodeViewSet)
router.register('spin', SpinViewSet)
router.register('wheel', WheelViewSet)
router.register('gift', GiftViewSet)


urlpatterns = [
    path('', include(router.urls))
]
