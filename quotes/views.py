from rest_framework.response import Response
from rest_framework.views import APIView

from quotes.models import Quote
from quotes.serializers import ReadQuoteSerializer

class GetRandomQuote(APIView):
    def get(self, request):
        lang = request.LANGUAGE_CODE
        quote = Quote.objects.order_by('?').only(f'text_{lang}', f'author_{lang}').first()
        serializer = ReadQuoteSerializer(quote, context={'request': request})
        return Response(serializer.data)
