from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView,
    UpdateView, DeleteView
)

from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 5
    
    def get_queryset(self):
        print('**************************')
        key_word = self.request.GET.get("kword", '')
        print('==============', key_word)
        lista = Empleado.objects.filter(
            full_name__icontains=key_word
        )
        return lista
    

class ListEmpleadosAdmin(ListView):
    template_name = 'empleados/empleados_admin.html'
    order_by = 'first_name'
    paginate_by = 5
    model = Empleado
    
    
class ListByAreaEmpleado(ListView):
    template_name = 'empleados/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['kword']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista

class ListEmpleadosByKeyword(ListView):
    """listar empleados por palabra clave."""
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('**************************')
        key_word = self.request.GET.get("kword", '')
        print('==============', key_word)
        lista = Empleado.objects.filter(
            first_name=key_word
        )
        print(lista)
        return lista

class ListHabilidadesAndEmpleados(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        key_word = self.request.GET.get("empleado", '')
        empleado = Empleado.objects.filter(
            first_name=key_word
        )
        print(empleado)
        habilidades = empleado[0].habilidades.all()
        return habilidades


class EmpleadoDetailView(DetailView):
    template_name = "empleados/detail_empleado.html"
    model = Empleado


class SuccesView(TemplateView):
    template_name = "empleados/succes.html"


class EmpleadoCreateView(CreateView):
    template_name = "empleados/add_empleado.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:list_empleados')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update_empleado.html"
    model = Empleado
    fields = [
        'first_name', 'last_name',
        'job', 'departamento',
        'habilidades', 'image'
    ]
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    template_name = "empleados/delete_empleado.html"
    model = Empleado
    success_url = reverse_lazy('empleado_app:empleados_admin')