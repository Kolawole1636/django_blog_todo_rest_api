from django.urls import path

from . import views

urlpatterns = [
    path('todolist', views.todolist,name="todolist"),
    path('createtodo', views.createtodo,name="createtodo"),
    path('deletetodo/<int:pk>', views.deletetodo,name="deletetodo"),
    path('updatetodo/<int:pk>', views.updatetodo,name="updatetodo"),
    path('todoApi/', views.todoApi,name="todoApi"),
    path('todoApiSingle/<int:pk>', views.todoApiSingle,name="todoApiSingle"),
    
]