

from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


#@login_required(login_url='/login')
def home(request):
    anio = datetime.now().year
    return render(request, 'base.html', {'anio': anio})


def salir(request):
    logout(request)
    return redirect('/login')

