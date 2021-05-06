# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.utils.translation import ugettext as _
from encrypted_fields import fields


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Card(BaseModel):
    name = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Nome'),
    )
    date = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Data'),
    )
    batch = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Lote'),
    )
    qty_records = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Qtd Registros'),
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Cartão')
        verbose_name_plural = _('Cartões')

    def __str__(self):
        return str(self.id)


class CardRow(BaseModel):
    card = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_('Cartão'),
    )
    tag = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Identificador da Linha'),
    )
    batch = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Númeração do Lote'),
    )
    number = fields.EncryptedCharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Número de Cartão Completo'),
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Linha do Cartão')
        verbose_name_plural = _('Linhas do Cartão')

    def __str__(self):
        return str(self.id)
