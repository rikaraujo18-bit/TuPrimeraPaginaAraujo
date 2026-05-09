from django.shortcuts import render, redirect, get_object_or_404
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

# NUEVAS FUNCIONES PARA EL TP4:

def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'veterinaria/listado_mascotas.html', {'mascotas': mascotas})

def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    return render(request, 'veterinaria/detalle_mascota.html', {'mascota': mascota})

def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('detalle_mascota', mascota_id=mascota.id)
    else:
        form = MascotaForm(instance=mascota)
    
    return render(request, 'veterinaria/editar_mascota.html', {'form': form, 'mascota': mascota})

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listado_mascotas')
    return render(request, 'veterinaria/eliminar_mascota.html', {'mascota': mascota})