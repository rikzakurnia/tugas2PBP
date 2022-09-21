from django.shortcuts import render

# TODO: Create your views here.
from mywatchlist.models import MovieWatchList

# Create your views here.
def show_watchlist(request):
    judul_movie_watchlist = MovieWatchList.objects.all()
    context = {
    'judul_movie': judul_movie_watchlist,
    'nama': 'Rikza Kurnia Almujtaba Lubis',
    'ID' : '2106701293'
    }
    return render(request, "mywatchlist.html", context)
