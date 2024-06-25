from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'creation_date', 'user')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description')
    actions = ['mark_as_completed']

    @admin.action(description='Marcar tareas seleccionadas como completadas')
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
