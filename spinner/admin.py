from django.contrib import admin

from .models import Gift, Wheel, Spin, Code


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    pass


@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
    pass


@admin.register(Spin)
class SpinAdmin(admin.ModelAdmin):
    pass


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    pass
