from django.urls import path
from todolist.views import show_todolist, show_todolist_json, register, login_user, create_task, toggle, delete, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name ='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create_task/', create_task, name='create_task'),
    path('toggle-task/<int:pk>', toggle, name='toggle'),
    path('delete-task/<int:pk>', delete, name='delete'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_todolist_json, name='show_todolist_json'),

]