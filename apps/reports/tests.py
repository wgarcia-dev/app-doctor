from django.test import RequestFactory, SimpleTestCase, override_settings

from apps.reports.views import PatientReportCSVView


class PatientReportFeatureFlagTests(SimpleTestCase):
    def test_report_is_not_available_when_feature_is_disabled(self):
        request = RequestFactory().get('/reports/patients/csv/')
        request.user = type('User', (), {'is_authenticated': True})()

        with override_settings(ENABLE_REPORTS=False):
            with self.assertRaisesMessage(Exception, 'La funcionalidad de reportes está desactivada.'):
                PatientReportCSVView.as_view()(request)
