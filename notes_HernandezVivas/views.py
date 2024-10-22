from django.views.generic.list import ListView
from notes_HernandezVivas.models import Note

#// from django.shortcuts import render
#// from django.http import HttpResponse
#//from django.views.generic.base import TemplateView

#// def home(request):
#//     return HttpResponse("Hola mundo")

#!note_list_HernandezVivas: Muestra todas las notas
class HomePageView(ListView):
    template_name = "notes/note_list_HernandezVivas.html"
    model = Note

#!note_detail_HernandezVivas.html: Mostrar una nota individual

#!note_create_HernandezVivas

#!note_edit_HernandezVivas.html: Crear/editar notas

#!note_delete_HernandezVivas.html: Eliminar notas
 