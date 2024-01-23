from django.contrib import admin
from django.contrib.admin import ModelAdmin

from tajriba.models import Tajriba


@admin.register(Tajriba)
class TajribaAdmin(ModelAdmin):
    list_display = ['name', 'started_at', 'ended_at', 'position']


