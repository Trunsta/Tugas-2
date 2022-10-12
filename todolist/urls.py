from venv import create
from django.urls import path
from todolist.views import delete_task, show_todolist, register, login_user, logout_user, create_task, change_status, delete_task, show_todolist_ajax, show_todolist_json, create_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path("change-status/<int:pk>/", change_status, name = "change_status"),
    path("delete-task/<int:pk>/", delete_task, name = "delete_task"),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', create_task_ajax, name='create_task_ajax'),
]