from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from apps.attention.forms.certificate import CertificateForm
from apps.attention.models import Certificado
from doctor.utils import save_audit


class CertificateCreateView(LoginRequiredMixin, CreateView):
    model = Certificado
    form_class = CertificateForm
    template_name = 'attention/certificate/form.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title='SaludSync', title1='Emitir certificado')
        return context

    def form_valid(self, form):
        form.instance.emitido_por = self.request.user
        response = super().form_valid(form)
        save_audit(self.request, self.object, action='A')
        messages.success(self.request, 'Certificado emitido. Ya puedes imprimirlo.')
        self.success_url = reverse_lazy('attention:certificate_detail', kwargs={'pk': self.object.pk})
        return response


class CertificateDetailView(LoginRequiredMixin, DetailView):
    model = Certificado
    template_name = 'attention/certificate/detail.html'
    context_object_name = 'certificado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(title='SaludSync')
        return context
