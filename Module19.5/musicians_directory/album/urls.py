from django.urls import path
from .import views

urlpatterns = [
    path('album/', views.AddAlbumView.as_view(), name = 'add_album'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name = 'edit_album'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name = 'delete_album'),
]
