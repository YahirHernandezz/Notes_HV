from django.urls import path
from notes_HernandezVivas.views import HomePageView, CreateNotaView, EditNotaView, DeleteNotaView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', CreateNotaView.as_view(), name='new'), #new/
    path('<int:pk>/edit', EditNotaView.as_view(), name='edit'), #`('<int:pk>/edit/')`
    path('<int:pk>/delete', DeleteNotaView.as_view(), name='delete'),
]