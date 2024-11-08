from rest_framework.response import Response
from rest_framework.views import APIView

from quotes.models import Quote
from quotes.serializers import ReadQuoteSerializer

class GetRandomQuote(APIView):
    def get(self, request):
        quote = Quote.objects.order_by('?').first()
        print("quote", quote)
        serializer = ReadQuoteSerializer(quote, context={'request': request})
        return Response(serializer.data)