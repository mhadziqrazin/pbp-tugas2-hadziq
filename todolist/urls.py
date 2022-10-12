from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, delete_task, update_status, todolist_ajax, get_todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>', delete_task, name='delete'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('json/', todolist_ajax, name='todolist_ajax'),
    path('get-todolist-json/', get_todolist_json, name='get_todolist_json')
]
