from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from maqola.models import Maqola, Menu, Tag


@admin.register(Tag)
class TagMaqolaAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Menu)
class MenuAdmin(TranslationAdmin):
    list_display = ['name', 'created_at']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Maqola)
class MaqolaAdmin(TranslationAdmin):
    list_display = ['name', 'menu', 'created_at', 'is_active']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
