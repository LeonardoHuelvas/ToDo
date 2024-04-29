from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True   

class Post(TimeStamped):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Campo de relación con el modelo de usuario
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
