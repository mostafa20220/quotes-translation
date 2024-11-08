from modeltranslation.translator import TranslationOptions, register

from quotes.models import Quote


@register(Quote)
class QuoteTranslationOptions(TranslationOptions):
    fields = ('author', 'text')