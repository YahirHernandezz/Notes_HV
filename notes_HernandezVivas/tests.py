from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_create_note(self):
        "Test creando una nota nueva"
        note = Note.objects.create(user=self.user, title="Proyecto final", content="Terminar el proyecto de Django antes de la fecha límite")
        self.assertEqual(note.title, "Proyecto final")
        self.assertEqual(note.content, "Terminar el proyecto de Django antes de la fecha límite")
        self.assertEqual(note.user, self.user)  

    def test_update_note(self):
        "Test para actualizar una nota que este lista ahí"
        note = Note.objects.create(user=self.user, title="Estudiar Python", content="Practicar funciones avanzadas")
        note.title = "Estudiar Python y Django"  
        note.content = "Practicar funciones avanzadas y repasar Django"  
        note.save()

        updated_note = Note.objects.get(id=note.id)
        self.assertEqual(updated_note.title, "Estudiar Python y Django")
        self.assertEqual(updated_note.content, "Practicar funciones avanzadas y repasar Django")

    def test_view_note_details(self):
        "Test pviendo el contenido de la nota"
        note = Note.objects.create(user=self.user, title="Preparar presentación", content="Terminar las diapositivas del proyecto")
        self.assertEqual(note.user, self.user)  
        self.assertEqual(note.title, "Preparar presentación")
        self.assertEqual(note.content, "Terminar las diapositivas del proyecto")

    def test_delete_note(self):
        "Test eliminando una nota existente"
        note = Note.objects.create(user=self.user, title="Comprar libros", content="Comprar biblia para la clase de cristianismo")
        note_id = note.id
        note.delete() 

        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)  

    def test_load_note_list(self):
        "Test mostrando la lista de notas"
        Note.objects.create(user=self.user, title="Visitar museo", content="Visitar el MIM este fin de semana")
        Note.objects.create(user=self.user, title="Hacer ejercicio", content="Ir al gimnasio y hacer brazo")

        notes = Note.objects.filter(user=self.user)
        self.assertEqual(notes.count(), 2)  

        titles = [note.title for note in notes]
        self.assertIn("Visitar museo", titles)
        self.assertIn("Hacer ejercicio", titles)

