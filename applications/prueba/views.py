from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView,

)

from .models import Prueba
from .forms import PruebaForm

class indexView(TemplateView):
    template_name = 'prueba/home.html'

class ModelPruebaListView(ListView):
    model = Prueba 
    template_name = 'prueba/pruebas.html'
    context_object_name = 'list_prueba'


class PruebaCreateView(CreateView):
    template_name = "prueba/add_prueba.html"
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy('prueba_app:listar_prueba')
