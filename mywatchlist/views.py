from django.shortcuts import render

from mywatchlist.models import MyWatchlist

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist_item = MyWatchlist.objects.all()
    context = {
        'data_watchlist': data_watchlist_item,
        'nama': 'Muhammad Hadziq Razin',
        'id': '2106707076',
    }
    return render(request, "mywatchlist.html", context)
