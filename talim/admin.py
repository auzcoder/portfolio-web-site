from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from talim.models import Talim


@admin.register(Talim)
class TajribaAdmin(TranslationAdmin):
    list_display = ['name', 'started_at', 'ended_at']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
