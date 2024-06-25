from django import forms
from .models import Task, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    """
    Formulario para crear y actualizar tareas.

    Attributes:
        Meta (class): Define el modelo y los campos que el formulario usará.
        __init__ (method): Personaliza la inicialización del formulario.
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['status'].widget = forms.Select(choices=Task.TASK_STATUSES)
        else:
            self.fields['status'].initial = 'pending'
            self.fields['status'].widget = forms.HiddenInput()


class SignupForm(UserCreationForm):
    """
    Formulario para el registro de nuevos usuarios.

    Attributes:
        Meta (class): Define el modelo y los campos que el formulario usará.
    """
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    """
    Formulario para el inicio de sesión de usuarios.

    Attributes:
        username (CharField): Nombre de usuario.
        password (CharField): Contraseña del usuario.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar la información del usuario.

    Attributes:
        Meta (class): Define el modelo y los campos que el formulario usará.
    """
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Formulario para actualizar el perfil del usuario.

    Attributes:
        Meta (class): Define el modelo y los campos que el formulario usará.
    """
    class Meta:
        model = Profile
        fields = ['profile_image']
