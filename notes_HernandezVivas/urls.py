from django.urls import path
from notes_HernandezVivas.views import HomePageView, CreateNotaView, EditNotaView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('note_create_HernandezVivas/', CreateNotaView.as_view(), name='new'), #new/
    path('note_edit_HernandezVivas/<int:pk>', EditNotaView.as_view(), name='edit'), #`('<int:pk>/edit/')`

]