import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Quiz, Pregunta, Opcion

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'practice/index.html', {'quizzes': quizzes})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'practice/quiz_view.html', {'quiz': quiz, "disable": False})

def calificar(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    opciones = [request.POST[elem] for elem in request.POST if elem.startswith('opcion')]
    lista = []
    if opciones:
        lista = [Opcion.objects.get(pk=elem).verdadero for elem in opciones]
    answers = {key: value for key, value in zip(opciones, map(lambda x: 1 if x else 0, lista))}
    return render(request, 'practice/quiz_view.html', {'quiz': quiz, 'disable': True, "respuestas": answers, "opciones": opciones})
