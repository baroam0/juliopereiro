
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import ArticuloForm
from .models import Articulo, Marca, Proveedor

from helpers.helpers import es_numerico


#@login_required(login_url='/login')
def listadoarticulo(request):
    if "txtBuscar" in request.GET:
        parametro = request.GET.get('txtBuscar')

        if es_numerico(parametro):
            articulos = Articulo.objects.filter(
            Q(pk=parametro) |
            Q(codigoaccess__icontains=parametro)             
        ).order_by('descripcion')
        else:
            marcas = Marca.objects.filter(descripcion__icontains=parametro)
            proveedores = Proveedor.objects.filter(descripcion__icontains=parametro)
            articulos = Articulo.objects.filter(
                Q(descripcion__icontains=parametro) |
                Q(marca__in=marcas) |
                Q(proveedor__in=proveedores) 
            ).order_by('descripcion')
    else:
        articulos = Articulo.objects.all().order_by('descripcion')
    paginador = Paginator(articulos, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(
        request,
        'articulos/articulo_list.html',
        {
            'resultados': resultados
        })


#@login_required(login_url='/login')
def nuevoarticulo(request):
    if request.POST:
        form = ArticuloForm(request.POST)
        if form.is_valid():
            marca = form.save(commit=False)
            try:
                marca.save()
                messages.success(request, "Se ha grabado los datos del articulo.")
                return redirect('/articulos/listado')
            except Exception as e:
                messages.warning(request, "Ha ocurrido un error.")
                return redirect('/articulos/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/articulos/listado')
    else:
        form = ArticuloForm()
        return render(
            request,
            'articulos/articulo_edit.html',
            {"form": form}
        )


#@login_required(login_url='/login')
def editararticulo(request, pk):
    consulta = Articulo.objects.get(pk=pk)

    if request.POST:
        form = ArticuloForm(request.POST, instance=consulta)
        if form.is_valid():
            marca= form.save(commit=False)
            marca.save()
            messages.success(request, "Se ha modificado los datos del articulo.")
            return redirect('/articulos/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/articulos/listado')
    else:
        form = ArticuloForm(instance=consulta)
        return render(
            request,
            'articulos/articulo_edit.html',
            {
                "form": form,
                "pk": consulta.pk
            }
        )

# Create your views here.


