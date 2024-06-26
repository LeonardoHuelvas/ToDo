from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, IndexView, SignupView, MyLoginView, MyLogoutView, profile

urlpatterns = [
    path('', IndexView.as_view(), name='index'),   
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='create-task'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('profile/', profile, name='profile'),


]
