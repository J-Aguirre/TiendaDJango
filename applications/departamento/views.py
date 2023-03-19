from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.empleados.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        nombre_departamento = form.cleaned_data['departamento']
        short_name_departamento = form.cleaned_data['short_name']
        departamento = Departamento(
            name = nombre_departamento,
            short_name = short_name_departamento
        )
        departamento.save()
        nombre_empleado = form.cleaned_data['nombre']
        apellido_empleado = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre_empleado,
            last_name = apellido_empleado,
            job = '1',
            departamento = departamento
        )
        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/list_all.html"