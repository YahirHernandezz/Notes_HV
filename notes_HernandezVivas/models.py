import datetime
from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario
from django.utils import timezone

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Título: {self.title} Contenido de la nota: {self.content}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)