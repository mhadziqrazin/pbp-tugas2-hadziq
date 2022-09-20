from django.shortcuts import render

from mywatchlist.models import MyWatchlist

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist_item = MyWatchlist.objects.all()
    count = 0
    for movie in data_watchlist_item:
        if movie.watched == "Already":
            count += 1
    if count >= 5:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    context = {
        'data_watchlist': data_watchlist_item,
        'nama': 'Muhammad Hadziq Razin',
        'id': '2106707076',
        'pesan': pesan
    }
    return render(request, "mywatchlist.html", context)
