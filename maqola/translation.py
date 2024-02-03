from modeltranslation.translator import TranslationOptions, register
from maqola.models import Menu, Maqola


@register(Menu)
class MenuTranslation(TranslationOptions):
    fields = ('name', )


@register(Maqola)
class MaqolaTranslation(TranslationOptions):
    fields = ('name', 'description', 'content')

