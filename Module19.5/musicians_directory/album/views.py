# Create class based views import file here.
from .import forms
from .import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# add ablum class based views
class AddAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('add_album')

# edit ablum class based views
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('add_album')
    pk_url_kwarg = 'id'

# delete album class based views
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'album/delete_album.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'