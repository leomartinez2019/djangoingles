from django.db import models

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.texto_pregunta

class Quiz(models.Model):
    tema = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300, default="Resuelve los ejercicios")
    fecha_creacion = models.DateTimeField('fecha de creacion', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('fecha de actualizacion', auto_now=True)
    preguntas = models.ManyToManyField(Pregunta)

    class Meta:
        ordering: ('tema')

    def __str__(self):
        return self.tema

class Opcion(models.Model):
    texto_opcion = models.CharField(max_length=200)
    verdadero = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        if self.verdadero:
            validez = "verdadero"
        else:
            validez = "falso"
        return f"{self.texto_opcion} es {validez}"
