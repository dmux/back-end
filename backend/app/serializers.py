# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
    CardRow, )


class CardRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardRow
        fields = [
            'id',
            'tag',
            'batch',
            'number',
        ]
