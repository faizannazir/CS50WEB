from django.urls import path

from . import views

urlpatterns = [
    path('',view=views.index,name="hello.index"),
    path('faizan', views.faizan,name="hello.faizan"),
    path('<str:name>', views.greet,name="hello.greet"),

]