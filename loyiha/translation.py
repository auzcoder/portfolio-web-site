from loyiha.models import Loyiha
from modeltranslation.translator import TranslationOptions, register


@register(Loyiha)
class TalimTranslation(TranslationOptions):
    fields = ('name', 'content')
