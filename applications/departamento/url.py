# from django.contrib import admin
from django.urls import path

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'nuevo-departamento/', 
        views.NewDepartamentoView.as_view(),
        name='nuevo_departamento'
    ),
    path(
        'listar-departamento',
        views.DepartamentoListView.as_view(),
        name='listar_departamentos'
    )
]