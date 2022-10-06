from django.shortcuts import render, redirect
from empleado.models import Empleado
from empleado.forms import EmpleadoForm

from crud.empleado.models import Empleado


# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
        else:
            form = Empleado()
        return render(request, 'index.html', {'form': form})


def show(request):
    empleado = Empleado.objects.all()
    return render(request, 'show.html', {'empleado': empleado})


def edit(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, 'edit.html', {'empleado': empleado})


def update(request, id):
    empleado = Empleado.objects.get(id=id)
    form = Empleado(request.POST, instance=empleado)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'empleado': empleado})


def eliminate(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("/show")
