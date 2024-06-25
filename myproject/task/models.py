from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Modelo que representa una tarea en la aplicación de lista de tareas.

    Attributes:
        user (ForeignKey): Relación con el modelo de usuario.
        title (CharField): Título de la tarea.
        description (TextField): Descripción detallada de la tarea.
        creation_date (DateTimeField): Fecha de creación de la tarea.
        status (CharField): Estado de la tarea (pendiente o completada).
    """
    TASK_STATUSES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TASK_STATUSES)

    def __str__(self):
        return self.title


class TimeStamped(models.Model):
    """
    Modelo abstracto que añade campos de marca de tiempo para creación y actualización.

    Attributes:
        created_at (DateTimeField): Fecha de creación del registro.
        updated_at (DateTimeField): Fecha de última actualización del registro.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True   


class Post(TimeStamped):
    """
    Modelo que representa una publicación.

    Attributes:
        author (ForeignKey): Relación con el modelo de usuario.
        title (CharField): Título de la publicación.
        content (TextField): Contenido de la publicación.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    """
    Modelo que representa el perfil de un usuario.

    Attributes:
        user (OneToOneField): Relación uno a uno con el modelo de usuario.
        profile_image (ImageField): Imagen de perfil del usuario.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
