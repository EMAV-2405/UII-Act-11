from django.urls import path
from . import views

app_name = 'app_vehiculosYservicios'

urlpatterns = [
    # URLs para Vehículos
    path('', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('vehiculo/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/editar/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/borrar/<int:vehiculo_id>/', views.borrar_vehiculo, name='borrar_vehiculo'),

    # URLs para Servicios (asociadas a un vehículo)
    path('vehiculo/<int:vehiculo_id>/servicio/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicio/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicio/borrar/<int:servicio_id>/', views.borrar_servicio, name='borrar_servicio'),
]