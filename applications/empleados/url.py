from django.urls import path

from . import views

app_name = "empleado_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='listar_empleados'),
    path(
        'empleados-admin/', 
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'),
    path(
        'listar-por-departamento/<kword>', 
        views.ListByAreaEmpleado.as_view(),
        name='listar_por_departamento'
    ),
    path('buscar-empleado/', views.ListEmpleadosByKeyword.as_view()),
    path('empleado-habilidades/', views.ListHabilidadesAndEmpleados.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='ver_empleado'
    ),
    path(
        'anadir-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='anadir_empleado'
    ),
    path(
        'exito/', 
        views.SuccesView.as_view(), 
        name='exito'
    ),
    path(
        'actualizar-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='actualizar_empleado'
    ),
    path(
        'borrar-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='borrar_empleado'
    ),
]