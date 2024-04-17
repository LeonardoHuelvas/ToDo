from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/task_create.html'  
    fields = ['title', 'description']  
    success_url = reverse_lazy('task-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_edit.html'  
    fields =  ['title', 'description' ]     
    success_url = reverse_lazy('task-list')
    
class TaskDeleteView(DeleteView):    
    model = Task
    template_name = 'task/task_delete.html'  
    success_url=reverse_lazy("task-list")