from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data = MyWatchList.objects.all()
    jml_film = 0
    for film in data:
        if(film.watched == "Yes"):
            jml_film+=1
    if(jml_film < 10 - jml_film):
        isi = "Wah, kamu masih sedikit menonton!"
    else:
        isi = "Selamat, kamu sudah banyak menonton!"
    context = {
        'MyWatchlist': data,
        'Nama': 'Ihza Dafa Maulidan',
        'NPM': '2106652726',
        'Message': isi
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id (request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")