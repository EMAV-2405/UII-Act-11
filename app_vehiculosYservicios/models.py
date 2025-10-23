from django.db import models

class Vehiculo(models.Model):
    # Django creará automáticamente un 'id' como clave primaria si no especificas uno.
    # Si quieres 'id_vehiculo' explícitamente como PK, puedes usar:
    # id_vehiculo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100, help_text="Modelo del vehículo (Ej: Ford Mustang)")
    año = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cant_disponible = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='vehiculos/', blank=True, null=True) # Carpeta 'vehiculos/' dentro de MEDIA_ROOT

    def __str__(self):
        return f"{self.modelo} ({self.año})"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

class ServicioMantenimiento(models.Model):
    # Django creará automáticamente un 'id' como clave primaria.
    # Si quieres 'id_servicio' explícitamente como PK, puedes usar:
    # id_servicio = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='servicios')
    # id_cliente (asumimos que un cliente puede ser un campo de texto simple por ahora)
    id_cliente = models.CharField(max_length=50, help_text="Identificador del cliente")
    tipo_servicio = models.CharField(max_length=100)
    fecha_servicio = models.DateField()
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=100)

    def __str__(self):
        return f"Servicio de {self.tipo_servicio} para {self.vehiculo.modelo} el {self.fecha_servicio}"

    class Meta:
        verbose_name = "Servicio de Mantenimiento"
        verbose_name_plural = "Servicios de Mantenimiento"