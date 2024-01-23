from talim.models import Talim
from modeltranslation.translator import TranslationOptions, register


@register(Talim)
class TajribaTranslation(TranslationOptions):
    fields = ('name', 'course', 'content')
