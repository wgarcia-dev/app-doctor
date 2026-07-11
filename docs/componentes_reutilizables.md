# Componentes reutilizables y específicos

## Alcance

Este análisis corresponde exclusivamente a la **Sección 1**. No se incorporan banderas de configuración, variantes de producto ni una aplicación de reportes, porque esas actividades pertenecen a las secciones 2 y 3.

## Tabla de clasificación

| Componente | Ubicación actual | Clasificación | Motivo y posibilidad de reutilización |
|---|---|---|---|
| Configuración y arranque Django | `doctor/settings.py`, `doctor/urls.py`, `manage.py` | Reutilizable con adaptación | Centraliza configuración, URLs raíz, estáticos y medios. Puede ser la base de otro proyecto Django, ajustando entorno, base de datos y apps instaladas. |
| Seguridad y autenticación | `apps/security/` y `django.contrib.auth` | Reutilizable | La app `security` está separada y registrada, lista para concentrar autenticación, perfiles y permisos. Actualmente la autenticación efectiva la proporciona `django.contrib.auth`; `security` aún no define vistas, URLs ni modelos propios. |
| Utilidades y validaciones | `doctor/utils.py`, `doctor/mixins.py` | Reutilizable | Validación de cédula, teléfono, números, serialización, IP del cliente y mixins CRUD son transversales. Se pueden trasladar a un paquete compartido tras desacoplar la auditoría de los modelos médicos. |
| Plantilla base y mensajes | `template/components/base.html`, `template/includes/` | Reutilizable | El layout, los mensajes y el modal de confirmación pueden reutilizarse en sistemas administrativos Django con cambio de identidad visual y navegación. |
| Gestión de archivos | `MEDIA_ROOT`, `MEDIA_URL`, campos `ImageField` y `FileField` | Reutilizable | La configuración de carga de fotos, currículos y firmas es transversal. Las rutas y políticas de almacenamiento deben adaptarse a cada despliegue. |
| Administración Django | `admin.py` de cada app y ruta `admin/` | Opcional | Facilita la administración de catálogos y registros. Es una funcionalidad de soporte que puede activarse o restringirse por proyecto y rol. |
| Gestión de pacientes y catálogos clínicos | `apps/core/` | Específico del dominio médico | Contiene pacientes, sangre, especialidades, doctores, empleados, medicamentos y diagnósticos; su modelo de datos responde al contexto clínico. |
| Atención clínica | `apps/attention/` | Específico del dominio médico | Modela horarios, citas, atenciones, prescripciones, servicios y costos. Depende de pacientes y diagnósticos del dominio. |
| Panel de inicio y navegación | `apps/core/views/home.py`, `template/components/base.html` | Específico con elementos reutilizables | Las métricas, accesos rápidos y enlaces actuales son clínicos. La estructura de plantilla sí es reutilizable. |
| Búsqueda y filtrado de listados | Vistas `PatientListView` y `AttentionListView` | Opcional | Es una mejora de experiencia que puede mantenerse, ampliarse o excluirse en otra instalación sin afectar el modelo clínico básico. |
| Exportación de PDF, notificaciones e integraciones externas | No implementado | Opcional futuro | No forma parte del código actual. Se recomienda aislar cada capacidad en una app propia si se incorpora posteriormente. |

## Adaptación de código realizada

Se eliminó de `apps/attention/urls.py` la importación de vistas de `core` que no se usaban. Con ello, el módulo de rutas de atención solo declara dependencias de su propia app, evitando un acoplamiento innecesario y haciendo más clara su posible reutilización.

La dependencia de `apps.attention.models` respecto a las entidades clínicas de `apps.core` se conserva deliberadamente: representa una relación de negocio real entre una atención, un paciente, diagnósticos y medicamentos.

## Fronteras recomendadas

- `apps/security`: autenticación, autorización, perfiles y auditoría transversal.
- `apps/core`: maestros clínicos y gestión de pacientes.
- `apps/attention`: flujo asistencial, citas, consulta y costos.
- `doctor`: configuración de proyecto y utilidades verdaderamente genéricas.
- `template/components` e `template/includes`: componentes visuales compartidos.

Para extraer un componente a otro proyecto, deben conservarse su `apps.py`, `models.py`, formularios, vistas, URLs, migraciones, plantillas y pruebas; después se registra su `AppConfig` en `INSTALLED_APPS` y se incluyen sus URLs en el proyecto destino.
