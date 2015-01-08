# -*- coding: utf-8 -*-

from django.contrib import admin
from ranklist.models import RankData


class RankDataAdmin(admin.ModelAdmin):
    list_display = ('word', 'site', 'url', 'time')
    list_filter = ['time']
    search_fields = ['word', 'site']

admin.site.register(RankData, RankDataAdmin)