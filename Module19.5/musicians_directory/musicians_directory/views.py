from django.shortcuts import render
from album.models import Album
from musician.models import Musician
from django.views.generic import DetailView

# album show class based views
class AlbumView(DetailView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        musician = Musician.objects.all()
        album = Album.objects.all().select_related('musician')
        return render(request, self.template_name, {'album': album, 'musician': musician})