import csv

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.views import View

from apps.core.models import Paciente


class PatientReportCSVView(LoginRequiredMixin, View):
    """Exporta el listado de pacientes sin incorporar lógica de reportes a core."""

    def get(self, request, *args, **kwargs):
        # La comprobación también protege el acceso si una URL se conserva por error.
        if not settings.ENABLE_REPORTS:
            raise Http404('La funcionalidad de reportes está desactivada.')

        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="reporte_pacientes.csv"'
        response.write('\ufeff')  # BOM para que Excel interprete correctamente UTF-8.

        writer = csv.writer(response)
        writer.writerow([
            'ID', 'Apellidos', 'Nombres', 'Cédula', 'Fecha de nacimiento',
            'Teléfono', 'Correo', 'Sexo', 'Activo',
        ])
        for patient in Paciente.objects.order_by('apellidos', 'nombres'):
            writer.writerow([
                patient.pk,
                patient.apellidos,
                patient.nombres,
                patient.cedula,
                patient.fecha_nacimiento.isoformat(),
                patient.telefono,
                patient.email or '',
                patient.get_sexo_display(),
                'Sí' if patient.activo else 'No',
            ])

        return response
