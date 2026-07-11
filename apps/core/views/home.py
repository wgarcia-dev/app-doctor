from django.views.generic import TemplateView
from django.db.models import DecimalField, Sum, Value
from django.db.models.functions import Coalesce
from django.utils import timezone
from apps.core.models import Paciente
from apps.attention.models import Atencion, CitaMedica, CostosAtencion

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        context = {"title": "SaludSync", "title1": "Sistema Médico", "title2": "Sistema Médico"}
        context['can_paci'] = Paciente.objects.filter(activo=True).count()
        context['citas_hoy'] = CitaMedica.objects.filter(fecha=today).exclude(estado='C').count()
        context['atenciones_hoy'] = Atencion.objects.filter(fecha_atencion__date=today).count()
        context['ingresos_hoy'] = CostosAtencion.objects.filter(fecha_pago__date=today, activo=True).aggregate(
            total=Coalesce(Sum('total'), Value(0), output_field=DecimalField())
        )['total']
        context['proximas_citas'] = CitaMedica.objects.select_related('paciente').filter(fecha__gte=today, estado='P').order_by('fecha', 'hora_cita')[:3]
        context['actividad_reciente'] = Atencion.objects.select_related('paciente').order_by('-fecha_atencion')[:3]
        return context
