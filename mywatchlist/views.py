from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist_item = MyWatchlist.objects.all()
    count = 0
    for movie in data_watchlist_item:
        if movie.watched == "Already":
            count += 1
    if count >= len(data_watchlist_item) - count:
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

def show_watchlist_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")