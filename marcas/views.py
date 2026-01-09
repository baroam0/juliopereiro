
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import MarcaForm
from .models import Marca


#@login_required(login_url='/login')
def listadomarca(request):
    if "txtBuscar" in request.GET:
        parametro = request.GET.get('txtBuscar')
        marcas = Marca.objects.filter(descripcion__contains=parametro).order_by('descripcion')
    else:
        marcas = Marca.objects.all().order_by('descripcion')
    paginador = Paginator(marcas, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(
        request,
        'marcas/marca_list.html',
        {
            'resultados': resultados
        })


#@login_required(login_url='/login')
def nuevamarca(request):
    if request.POST:
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca = form.save(commit=False)
            try:
                marca.save()
                messages.success(request, "Se ha grabado los datos de la marca.")
                return redirect('/marca/listado')
            except Exception as e:
                messages.warning(request, "Ha ocurrido un error.")
                return redirect('/marca/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/marca/listado')
    else:
        form = MarcaForm()
        return render(
            request,
            'marcas/marca_edit.html',
            {"form": form}
        )


#@login_required(login_url='/login')
def editarmarca(request, pk):
    consulta = Marca.objects.get(pk=pk)

    if request.POST:
        form = MarcaForm(request.POST, instance=consulta)
        if form.is_valid():
            marca= form.save(commit=False)
            marca.save()
            messages.success(request, "Se ha modificado los datos de la marca.")
            return redirect('/marca/listado')
        else:
            messages.warning(request, form.errors["__all__"])
            return redirect('/marca/listado')
    else:
        form = MarcaForm(instance=consulta)
        return render(
            request,
            'marcas/marca_edit.html',
            {"form": form}
        )

# Create your views here.
