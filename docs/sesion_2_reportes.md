# Sesión 2: funcionalidad opcional de reportes

La funcionalidad opcional se implementó como la app independiente `apps.reports`. Exporta un listado de pacientes en formato CSV, compatible con Excel y LibreOffice, sin añadir dependencias externas.

## Activación y desactivación

En `doctor/settings.py` se controla con:

```python
ENABLE_REPORTS = True
```

- Con `True`, se publica `/reports/patients/csv/` y aparece el botón **Exportar reporte CSV** en la lista de pacientes.
- Con `False`, no se publica esa ruta y el botón desaparece. La vista además verifica la bandera y responde con 404 si se invocara directamente.

## Capturas requeridas

1. Inicia el servidor con `ENABLE_REPORTS = True`, abre **Pacientes** y captura la pantalla donde se ve el botón **Exportar reporte CSV**.
2. Cambia a `ENABLE_REPORTS = False`, reinicia el servidor, abre la misma pantalla y captura el resultado sin ese botón.

La comparación de ambas imágenes demuestra la variabilidad solicitada sin modificar la funcionalidad base de pacientes.
