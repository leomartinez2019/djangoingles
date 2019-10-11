from pyquiz.models import Quiz, Opcion, Pregunta

def crear_pregunta(texto):
    pregunta = Pregunta()
    pregunta.texto_pregunta = texto
    pregunta.save()
    print(f"Pk de la pregunta: {pregunta.pk}")

def crear_quiz(tema, descripcion):
    quiz = Quiz(tema=tema, descripcion=descripcion)
    quiz.save()
    print(f"Pk del quiz: {quiz.pk}")

def agregar_pregunta_al_quiz(pregunta, quiz):
    quiz.preguntas.add(pregunta)
    print(f"Pk del quiz: {quiz.pk}, pk de la pregunta {pregunta.pk}")

def crear_opcion(texto, pregunta):
    opcion = Opcion(texto_opcion=texto, pregunta=pregunta)
    opcion.save()

# Ejemplo de texto a Procesar:
# tema
# descripcion
# ?
# pregunta1
# *
# opcion1
# $opcion-verdadera
# opcion3
def crear_cuestionario_desde_archivo(archivo):
    'procesa texto de acuerdo a ciertas cadenas'
    with open(archivo, 'r') as file_handler:
        content = file_handler.read()
    lista = content.split("\n")
    # Las dos primeras lineas son para quiz
    q = Quiz(tema=lista[0], descripcion=lista[1])
    q.save()
    print(q)
    crear_pregunta = False
    crear_opcion = False
    for elem in lista[2:]:
        if elem == '!': # salir
            break
        if elem == '?': # inicia pregunta
            crear_pregunta = True
            crear_opcion = False
            continue
        if crear_pregunta:
            p = Pregunta(texto_pregunta=elem)
            p.save()
            q.preguntas.add(p)
            print(p)
            crear_pregunta = False
        if elem == '*': # inicia opcion
            crear_opcion = True
            continue
        if crear_opcion:
            if elem.startswith("$"): # opcion verdera
                opcion = Opcion(texto_opcion=elem[1:], verdadero=True, pregunta=p)
            else:
                opcion = Opcion(texto_opcion=elem, pregunta=p)
            opcion.save()
            print(opcion)
