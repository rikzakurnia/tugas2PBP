from django.shortcuts import render

# TODO: Create your views here.
from mywatchlist.models import MovieWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    list_movie_watchlist = MovieWatchList.objects.all()
    context = {
    'list_movie': list_movie_watchlist,
    'nama': 'Rikza Kurnia Almujtaba Lubis',
    'ID' : '2106701293'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    list_movie_watchlist = MovieWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", list_movie_watchlist), content_type="application/xml")

def show_json(request):
    list_movie_watchlist = MovieWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", list_movie_watchlist), content_type="application/json")