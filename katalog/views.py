from django.shortcuts import render

from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_catalog': data_catalog_item,
        'nama': 'Muhammad Hadziq Razin',
        'id': '2106707076',
    }
    return render(request, "katalog.html", context)
