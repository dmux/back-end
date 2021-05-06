# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Card,
    CardRow,
)


class CardRowInLineAdmin(admin.StackedInline):
    model = CardRow
    extra = 0
    classes = ['collapse']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date',
        'batch',
        'qty_records',
    )
    inlines = [
        CardRowInLineAdmin,
    ]
