from django.contrib import admin
from django.urls import path

from quotes.views import GetRandomQuote

urlpatterns = [
    path('', GetRandomQuote.as_view(), name='quote'),
]
