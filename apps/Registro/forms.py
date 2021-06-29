from django import forms
from django.forms import widgets
from .models import Proveedor, Plato


class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = ['nombre', 'precio', 'ingredientes',
                  'descripcion', 'proveedor', 'imagen']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'ingredientes': 'Ingredientes',
            'descripcion': 'Descripcion',
            'proveedor': 'Proveedor',
            'imagen': 'Imagen',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
        }


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre Proveedor',
            'email': 'Correo Electronico',
            'numero': 'Numero Contacto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }