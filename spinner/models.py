from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), blank=True, null=True)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)

    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class Gift(AbstractModel):
    possibility = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _('gift')
        verbose_name_plural = _('gifts')


class Wheel(AbstractModel):
    gifts = models.ManyToManyField(Gift, related_name='wheels', verbose_name=_('gifts'))

    class Meta:
        verbose_name = _('wheel')
        verbose_name_plural = _('wheels')


class Spin(AbstractModel):
    user = models.CharField(max_length=255, verbose_name=_('user nickname'))
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE, related_name='spins', verbose_name=_('wheel'))
    prize = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name='prizes', verbose_name=_('prize'))

    class Meta:
        verbose_name = _('spin')
        verbose_name_plural = _('spins')


class Code(AbstractModel):
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE, related_name='codes', verbose_name=_('wheel'))
    spins_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('code')
        verbose_name_plural = _('codes')
