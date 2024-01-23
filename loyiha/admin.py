from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from loyiha.models import Loyiha, Texnologiyalar


@admin.register(Texnologiyalar)
class TexnologiyalarAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


# @admin.register(Tajriba)
# class TajribaAdmin(TranslationAdmin):
#     list_display = ['name', 'started_at', 'ended_at', 'center']
#
#     class Media:
#         js = (
#             'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }

