from sertifikat.models import Sertifikat
from modeltranslation.translator import TranslationOptions, register


@register(Sertifikat)
class TalimTranslation(TranslationOptions):
    fields = ('name', 'description')
