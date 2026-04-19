from django.shortcuts import render, redirect
from .models import Cliente, Mascota, Consulta
from .forms import ClienteForm, MascotaForm, ConsultaForm, BuscarMascotaForm

def inicio(request):
    return render(request, 'veterinaria/inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'veterinaria/agregar_cliente.html', {'form': form})

def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MascotaForm()
    return render(request, 'veterinaria/agregar_mascota.html', {'form': form})

def agregar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ConsultaForm()
    return render(request, 'veterinaria/agregar_consulta.html', {'form': form})

def buscar_mascota(request):
    resultados = []
    form = BuscarMascotaForm(request.GET or None)
    
    if form.is_valid():
        nombre_buscado = form.cleaned_data['nombre']
        resultados = Mascota.objects.filter(nombre__icontains=nombre_buscado)
    
    return render(request, 'veterinaria/buscar_mascota.html', {
        'form': form,
        'resultados': resultados
    })