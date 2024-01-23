from talim.models import Talim
from modeltranslation.translator import TranslationOptions, register


@register(Talim)
class TalimTranslation(TranslationOptions):
    fields = ('name', 'course', 'content')
