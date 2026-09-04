from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto, Tarea

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def proyecto_detalle(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    return render(request, 'detalle_proyecto.html',{'proyecto': proyecto})

def nuevo_proyecto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        if nombre and descripcion and duracion:
            proyecto = Proyecto(
                nombre=nombre,
                descripcion=descripcion,
                duracion=duracion,
            )
            proyecto.save()
            return redirect('proyectos')  
          
    return render(request, 'nuevo_proyecto.html')

def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')


def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        proyecto.nombre = nombre
        proyecto.descripcion = descripcion
        proyecto.duracion = duracion
        
        # 1. Agregamos los paréntesis () para ejecutar el guardado
        proyecto.save() 
        
        return redirect('proyectos')

    # 2. Metemos el diccionario DENTRO del render (sin la coma afuera)
    return render(request, 'editar_proyecto.html', {'proyecto': proyecto})

def crear_tarea(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        prioridad = request.POST.get('prioridad')
        estado = request.POST.get('estado')

        if titulo:
            Tarea.objects.create(
                proyecto=proyecto,
                titulo=titulo,
                prioridad=prioridad,
                estado=estado
            )
            return redirect ('proyecto_detalle' , id=proyecto_id)
    return render(request, 'crear_tarea.html' , {'proyecto': proyecto, 'prioridad_choices':Tarea.PRIORIDAD_CHOICES, 'estado_choices': Tarea.ESTADO_CHOICES})