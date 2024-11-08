from django.utils import translation
from rest_framework import serializers

from quotes.models import Quote

class ReadQuoteSerializer(serializers.ModelSerializer):
    # text = serializers.SerializerMethodField()
    # author = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = ['text', 'author']
    #
    # def get_text(self, obj):
    #     lang = self.context.get('request').LANGUAGE_CODE
    #     return getattr(obj, f'text_{lang}')
    #
    # def get_author(self, obj):
    #     lang = self.context.get('request').LANGUAGE_CODE
    #     return getattr(obj, f'author_{lang}')
    #
