# -*- coding: utf-8 -*-

from ranklist.models import RankData
from rest_framework import serializers


class RankDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankData
        fields = ('word', 'site')