from django.urls import path

from . import views

urlpatterns = [    

    path('user_login', views.user_login, name='user login'),
    path('get_all_users', views.get_all_users, name='get all users'),
    path('create_user', views.create_user, name='create user'),
    path('get_user/<str:id>', views.get_user, name='get user by id user'),
    path('update_user/<str:id>', views.update_user, name='update user by id user'),
    path('delete_user/<str:id>', views.delete_user, name='delete user by id user'),


    path('get_all_todos', views.get_all_todos, name='get all users'),
    path('create_todo', views.create_todo, name='create user'),
    path('get_todo/<str:id>', views.get_todo, name='get user by id user'),
    path('update_todo/<str:id>', views.update_todo, name='update user by id user'),
    path('delete_todo/<str:id>', views.delete_todo, name='delete user by id user'),
    
]