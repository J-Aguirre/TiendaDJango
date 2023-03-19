from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        widgets = {
            'cantidad': forms.NumberInput(
                attrs = {
                    'placeholder': 'Coloque su cantidad'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Cantidad debe ser mayor a 10')
        return cantidad

    
            
