from django import forms
from .models import Cliente, Mascota, Consulta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'dueno']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['mascota', 'motivo', 'diagnostico']

class BuscarMascotaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre de la mascota")