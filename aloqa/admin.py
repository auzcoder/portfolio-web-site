from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from aloqa.models import Contact, About, SocialMedia


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'email', 'created_at']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'created_at']


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['fullname', 'position', 'created_at']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }