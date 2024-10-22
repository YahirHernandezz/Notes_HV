from django.urls import path
from notes_HernandezVivas.views import HomePageView, CreateNotaView, EditNotaView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', CreateNotaView.as_view(), name='new'), #new/
    path('<int:pk>/edit', EditNotaView.as_view(), name='edit'), #`('<int:pk>/edit/')`

]