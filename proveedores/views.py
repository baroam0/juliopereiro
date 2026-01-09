
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import ProveedorForm
from .models import Proveedor


#@login_required(login_url='/login')
def listadoproveedor(request):
    if "txtBuscar" in request.GET:
        parametro = request.GET.get('txtBuscar')
        marcas = Proveedor.objects.filter(descripcion__contains=parametro).order_by('descripcion')
    else:
        marcas = Proveedor.objects.all().order_by('descripcion')
    paginador = Paginator(marcas, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(
        request,
        'proveedores/proveedor_list.html',
        {
            'resultados': resultados
        })


#@login_required(login_url='/login')
def nuevoproveedor(request):
    if request.POST:
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            try:
                proveedor.save()
                messages.success(request, "Se ha grabado los datos del proveedor.")
                return redirect('/proveedor/listado')
            except Exception as e:
                messages.warning(request, "Ha ocurrido un error.")
                return redirect('/proveedor/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/proveedor/listado')
    else:
        form = ProveedorForm()
        return render(
            request,
            'proveedores/proveedor_edit.html',
            {"form": form}
        )


#@login_required(login_url='/login')
def editarproveedor(request, pk):
    consulta = Proveedor.objects.get(pk=pk)

    if request.POST:
        form = ProveedorForm(request.POST, instance=consulta)
        if form.is_valid():
            marca= form.save(commit=False)
            marca.save()
            messages.success(request, "Se ha modificado los datos del proveedor.")
            return redirect('/proveedor/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/proveedor/listado')
    else:
        form = ProveedorForm(instance=consulta)
        return render(
            request,
            'proveedores/proveedor_edit.html',
            {"form": form}
        )

# Create your views here.
