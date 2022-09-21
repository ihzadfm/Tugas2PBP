from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    datamywatchlist = MyWatchList.objects.all()
    count = 0
    for film in datamywatchlist:
        if film.is_watched == "Yes":
            count += 1
    if count >= 5:
        isi = "Selamat, kamu sudah banyak menonton!"
    else:
        isi = "Wah, kamu masih sedikit menonton!"

    context = {
        'mywatchlist': datamywatchlist,
        'nama': 'Ihza Dafa Maulidan',
        'npm': '2106652726',
        'pesan': isi
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")