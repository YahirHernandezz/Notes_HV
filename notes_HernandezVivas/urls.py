from django.urls import path
from notes_HernandezVivas.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]