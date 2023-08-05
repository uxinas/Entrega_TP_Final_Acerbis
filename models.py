from django.db import models

class Entradas_Blog(models.Model):
    Nombre = models.CharField(max_length=30)
    Fecha = models.DateField()
    Titulo = models.CharField(max_length=50)
    Subtitulo = models.CharField(max_length=50)
    Post = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Nombre: {self.Nombre} - Fecha {self.Fecha} - Titulo {self.Titulo} - Subtitulo {self.Subtitulo} - Post {self.Post}"
