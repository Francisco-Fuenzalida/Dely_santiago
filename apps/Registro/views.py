from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlatoForm, ProveedorForm
from .models import Plato, Proveedor
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# Metodo que agregara un plato a la BD
@permission_required('Registro.add_plato')
def agregar_plato(request):
    data = {
        'form': PlatoForm()
    }
    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data['form'] = formulario
    return render(request, 'registro/agregar_plato.html', data)

# Metoro que obtiene todos los platos de la BD
@permission_required('Registro.view_plato')
def listar_platos(request):
    platos = Plato.objects.all()
    # Agregando paginador
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(platos, 8)
        platos = paginator.page(page)
    except:
        raise Http404
    # -----------------------------------
    data = {
        'entity': platos,
        'paginator': paginator,
    }
    return render(request, 'registro/listado_platos.html', data)

# Metodo para editar un plato existente en la BD seleccionandolo por su ID
@permission_required('Registro.change_plato')
def editar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    data = {
        'form': PlatoForm(instance=plato)
    }
    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, instance=plato, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to='listado_platos')
        data["form"]= formulario
    return render(request, 'registro/editar_plato.html', data)

# Metodo para eliminar un plato
@permission_required('Registro.delete_plato')
def eliminar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    plato.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listado_platos')

# Metodo para agregar un proveedor
@permission_required('Registro.add_proveedor')
def agregar_proveedor(request):
    data = {
        'form': ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data['form'] = formulario
    return render(request, 'registro/agregar_proveedor.html', data)

# Metoro que obtiene todos los proveedores de la BD
@permission_required('Registro.view_proveedor')
def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    # Agregando paginador
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(proveedores, 8)
        proveedores = paginator.page(page)
    except:
        raise Http404
    # -----------------------------------
    data = {
        'entity': proveedores,
        'paginator': paginator,
    }
    return render(request, 'registro/listado_proveedores.html', data)

# Metodo para editar un plato existente en la BD seleccionandolo por su ID
@permission_required('Registro.change_proveedor')
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    data = {
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to='listado_proveedores')
        data["form"]= formulario
    return render(request, 'registro/editar_proveedor.html', data)

# Metodo para eliminar un plato
@permission_required('Registro.delete_proveedor')
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listado_proveedores')

# Metodo del cual se alimenta la tienda
def tienda(request):
    platos = Plato.objects.all()
    data = {
        'platos': platos
    }
    return render(request, 'tienda/tienda.html', data)