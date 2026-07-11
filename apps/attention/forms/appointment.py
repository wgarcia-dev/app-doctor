from django import forms

from apps.attention.models import CitaMedica


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ('paciente', 'fecha', 'hora_cita', 'estado')
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_cita': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].initial = 'P'
        self.fields['paciente'].queryset = self.fields['paciente'].queryset.filter(activo=True)
