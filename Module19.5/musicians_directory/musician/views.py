# Create class based views import file here.
from .import forms
from .import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#add musician class based views 
class AddMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('add_musician')

#edit musician class based views 
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

#delete musician class based views 
# class DeleteMusicianView(DeleteView):
#     model = models.Musician
#     template_name = 'musician/musician_delete.html'
#     success_url = reverse_lazy('homepage')
#     pk_url_kwarg = 'id'