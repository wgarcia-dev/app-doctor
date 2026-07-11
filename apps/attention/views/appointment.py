from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.attention.forms.appointment import AppointmentForm
from apps.attention.models import CitaMedica
from doctor.utils import save_audit


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = CitaMedica
    form_class = AppointmentForm
    template_name = 'attention/appointment/form.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title='SaludSync', title1='Programar nueva cita')
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        save_audit(self.request, self.object, action='A')
        messages.success(self.request, 'La cita fue programada correctamente.')
        return response
