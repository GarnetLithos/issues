# -*- coding: utf-8 -*-

from django.db import models


class RankData(models.Model):
    word = models.CharField(max_length=20)
    site = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.word