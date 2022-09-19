from django.urls import path
from mywatchlist.views import show_watchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
]
