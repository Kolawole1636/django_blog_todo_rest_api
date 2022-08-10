from django.urls import path

from . import views

urlpatterns = [
    path('cal', views.calculator,name="calculator"),
    path('add', views.add,name="add"),
    
]