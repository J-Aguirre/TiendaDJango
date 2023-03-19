from django.urls import path

from . import views

app_name = 'prueba_app'

urlpatterns = [
    path('home/', views.indexView.as_view()),
    path(
        'listar-prueba/', 
        views.ModelPruebaListView.as_view(),
        name = 'listar_prueba'),
    path(
        'crear-prueba/', 
        views.PruebaCreateView.as_view(),
        name = "crear_prueba"
    )
]