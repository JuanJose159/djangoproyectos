from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    imagen = models.ImageField(upload_to='proyectos/' , default='proyectos/logo.png')


class Tarea (models.Model):
    '''
    MODELO QUE RESPRESENTA UNA TAREA DE UN PROYECTO
    '''

    PRIORIDAD_CHOICES =[
        ('BAJA','Baja'),
        ('MEDIA','Media'),
        ('ALTA', 'Alta'),
    ]

    ESTADO_CHOICES =[
            ('PENDIENTE','Pendiente'),
            ('EN_PROGRESO','En progreso'),
            ('COMPLETADA', 'Completada'),
        ]
    
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name="tareas"
    )


    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA'
    )
    estado = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='PENDIENTE'
    )