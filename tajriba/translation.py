from tajriba.models import Tajriba
from modeltranslation.translator import TranslationOptions, register


@register(Tajriba)
class TajribaTranslation(TranslationOptions):
    fields = ('name', 'position', 'content')
