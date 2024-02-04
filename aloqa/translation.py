from modeltranslation.translator import TranslationOptions, register
from aloqa.models import About


@register(About)
class AboutTranslation(TranslationOptions):
    fields = ('fullname', 'position', 'manzil', 'content', 'biography')
