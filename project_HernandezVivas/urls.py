from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes_HernandezVivas/', include('notes_HernandezVivas.urls')),
]
