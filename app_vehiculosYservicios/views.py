from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo, ServicioMantenimiento
from .forms import VehiculoForm, ServicioMantenimientoForm

# Vistas para Vehículos
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('modelo')
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    # Los servicios se acceden directamente a través de related_name='servicios'
    servicios = vehiculo.servicios.all().order_by('-fecha_servicio')
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo, 'servicios': servicios})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES) # ¡IMPORTANTE! request.FILES para subir imágenes
        if form.is_valid():
            form.save()
            return redirect('app_vehiculosYservicios:listar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'formulario_vehiculo.html', {'form': form, 'titulo': 'Registrar Nuevo Vehículo'})

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo) # request.FILES e instance
        if form.is_valid():
            form.save()
            return redirect('app_vehiculosYservicios:detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'formulario_vehiculo.html', {'form': form, 'titulo': f'Editar Vehículo: {vehiculo.modelo}'})

def borrar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('app_vehiculosYservicios:listar_vehiculos')
    return render(request, 'confirmar_borrar_vehiculo.html', {'vehiculo': vehiculo})

# Vistas para Servicios de Mantenimiento (asociados a un vehículo)
def crear_servicio(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = ServicioMantenimientoForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False) # No guarda aún, asignamos el vehículo
            servicio.vehiculo = vehiculo
            servicio.save()
            return redirect('app_vehiculosYservicios:detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = ServicioMantenimientoForm(initial={'vehiculo': vehiculo}) # Pre-selecciona el vehículo
    return render(request, 'formulario_servicio.html', {'form': form, 'vehiculo': vehiculo, 'titulo': f'Registrar Servicio para {vehiculo.modelo}'})

def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(ServicioMantenimiento, id=servicio_id)
    vehiculo = servicio.vehiculo # Obtenemos el vehículo asociado para la redirección
    if request.method == 'POST':
        form = ServicioMantenimientoForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('app_vehiculosYservicios:detalle_vehiculo', vehiculo_id=vehiculo.id)
    else:
        form = ServicioMantenimientoForm(instance=servicio)
    return render(request, 'formulario_servicio.html', {'form': form, 'vehiculo': vehiculo, 'titulo': f'Editar Servicio para {vehiculo.modelo}'})

def borrar_servicio(request, servicio_id):
    servicio = get_object_or_404(ServicioMantenimiento, id=servicio_id)
    vehiculo = servicio.vehiculo # Obtenemos el vehículo asociado
    if request.method == 'POST':
        servicio.delete()
        return redirect('app_vehiculosYservicios:detalle_vehiculo', vehiculo_id=vehiculo.id)
    return render(request, 'confirmar_borrar_servicio.html', {'servicio': servicio, 'vehiculo': vehiculo})