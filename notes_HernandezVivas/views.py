from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from notes_HernandezVivas.models import Note
from django.views.generic.edit import CreateView, UpdateView

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

#?note_create_HernandezVivas
class CreateNotaView(LoginRequiredMixin, CreateView):
    template_name = "notes/note_create_HernandezVivas.html"
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

#!note_edit_HernandezVivas.html: Crear/editar notas
class EditNotaView(UpdateView):
    template_name = 'notes/note_edit_HernandezVivas.html'
    model = Note
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse_lazy('home')

#?note_delete_HernandezVivas.html: Eliminar notas
 