from django import forms

from apps.attention.models import Atencion, Certificado


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ('paciente', 'atencion', 'motivo')
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'atencion': forms.Select(attrs={'class': 'form-select'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Indique la constancia o recomendación médica que se certifica.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].queryset = self.fields['paciente'].queryset.filter(activo=True)
        self.fields['atencion'].queryset = Atencion.objects.select_related('paciente').all()
        self.fields['atencion'].required = False
