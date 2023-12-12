from django.shortcuts import render
from album.models import Album
from musician.models import Musician

def home(request):
    musician = Musician.objects.all()
    album = Album.objects.all().select_related('musician')
    return render(request, 'home.html', {'album': album, 'musician': musician})
