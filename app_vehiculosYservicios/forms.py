from django import forms
from .models import Vehiculo, ServicioMantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['modelo', 'año', 'color', 'precio', 'cant_disponible', 'foto']
        # Widget para el campo de imagen para que no muestre la ruta completa,
        # aunque en este caso Django ya lo maneja bien por defecto para ImageField.
        # widgets = {
        #     'foto': forms.ClearableFileInput(),
        # }

class ServicioMantenimientoForm(forms.ModelForm):
    # Opcional: Personalizar el campo de fecha para usar un widget de tipo calendario
    fecha_servicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha del Servicio"
    )

    class Meta:
        model = ServicioMantenimiento
        fields = ['vehiculo', 'id_cliente', 'tipo_servicio', 'fecha_servicio', 'costo_servicio', 'proveedor']