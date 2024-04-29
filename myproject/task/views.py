from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, SignupForm, LoginForm

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    def dispatch(self, request, *args, **kwargs):
  
        if not request.user.is_authenticated:
       
            context = {'message': 'Debes iniciar sesión para ver esta página.'}
            return render(request, 'error_message.html', context, status=401)
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(user=self.request.user)
        

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
 

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_edit.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('task-list')

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'login/signup.html', {'form': form})    

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
        
            return redirect('login')  
        return render(request, 'login/signup.html', {'form': form})
    
class MyLoginView(View):
    template_name = 'login/login.html'  

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})    

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
              
                return render(request, self.template_name, {
                    'form': form,
                    'error_message': 'Usuario o contraseña incorrectos.'
                })
        return render(request, self.template_name, {'form': form})


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
