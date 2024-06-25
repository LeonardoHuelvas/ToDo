markdown

## Authors

- [@lejhubo](https://github.com/LeonardoHuelvas)

# 📋 Proyecto Integrador - To Do App Django

## 📖 Descripción
Esta aplicación web de lista de tareas está construida con Django 🐍 y permite a los usuarios gestionar sus tareas diarias. Los usuarios pueden crear ✏️, visualizar 👀, editar 📝 y eliminar ❌ tareas, todo dentro de una interfaz intuitiva y segura 🔒.

## 🚀 Cómo empezar

### 🔧 Requisitos previos
- Python 3.12 🐍
- pip 📦 (Python package installer)

### 🛠 Configuración del entorno
Para ejecutar este proyecto, instala las dependencias en un entorno virtual:

```bash
python -m venv myenv
source myenv/bin/activate # En Windows use `myenv\Scripts\activate`
pip install -r requirements.txt

🗃 Configuración de la base de datos

Realiza las migraciones necesarias para configurar la base de datos:

bash

python manage.py makemigrations
python manage.py migrate

👤 Creación de un superusuario

Crea un superusuario para acceder al panel de administración de Django:

bash

python manage.py createsuperuser

🌐 Ejecución del servidor de desarrollo

Para iniciar el servidor de desarrollo, ejecuta:

bash

python manage.py runserver

El servidor estará disponible en: http://127.0.0.1:8000/task/list
📂 Estructura del proyecto

    task/: Aplicación Django que contiene el modelo Task y vistas para CRUD.
    templates/: Contiene archivos HTML para el sistema de templates de Django.
    manage.py: Script de utilidad para administrar el proyecto Django.

🌈 Referencia de Colores
Color	Hex
Ejemplo Color 1	#0a192f #0a192f
Ejemplo Color 2	#f8f8f8 #f8f8f8
Ejemplo Color 3	#00b48a #00b48a
Ejemplo Color 4	#00d1a0 #00d1a0
🚀 Sobre Mí

Soy un desarrollador full stack apasionado por la tecnología y la música. Toco la guitarra en mi tiempo libre y actualmente soy estudiante de Protalento.
⚡️ Dato Curioso

¡Me apasiona la música y toco la guitarra en mi tiempo libre!
🎓 Educación

Soy estudiante de Protalento.
📜 Licencia

MIT