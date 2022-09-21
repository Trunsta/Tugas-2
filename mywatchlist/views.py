from django.shortcuts import render
from mywatchlist.models import WatchListAttribute

from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    data_watchlist = WatchListAttribute.objects.all()
    watchlist_len = len(data_watchlist)
    watched_len = len(WatchListAttribute.objects.filter(watched = "Yes"))
    watched = False

    if (watched_len >= watchlist_len/2):
        watched = True

    context = {
        'data_watchlist' : data_watchlist,
        'watched' : watched
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watchlist = WatchListAttribute.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_json(request):
    data_watchlist = WatchListAttribute.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")    