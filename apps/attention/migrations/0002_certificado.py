from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('attention', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField(verbose_name='Contenido del certificado')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')),
                ('atencion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificados', to='attention.atencion', verbose_name='Atención relacionada')),
                ('emitido_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificados_emitidos', to=settings.AUTH_USER_MODEL, verbose_name='Emitido por')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='certificados', to='core.paciente', verbose_name='Paciente')),
            ],
            options={'verbose_name': 'Certificado', 'verbose_name_plural': 'Certificados', 'ordering': ['-fecha_emision']},
        ),
    ]
