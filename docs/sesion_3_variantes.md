# Sesión 3: configuración de variabilidad

## Variantes implementadas

Las variantes se definen en `doctor/config_product.py`. `doctor/settings.py` lee la variable de entorno `PRODUCT_VARIANT`, selecciona la configuración correspondiente y expone las banderas que consume el sistema.

| Variante | `PRODUCT_VARIANT` | `ENABLE_REPORTS` | `ENABLE_NOTIFICATIONS` | Resultado |
|---|---:|---:|---:|---|
| A: básica | `A` | `False` | `False` | Gestión clínica base sin exportación de reportes ni notificaciones extendidas. |
| B: completa | `B` | `True` | `True` | Gestión clínica base más exportación CSV de pacientes y notificaciones habilitadas para extensiones del producto. |

## Cómo cambiar de variante

En el archivo `.env`, agrega o modifica esta línea:

```env
PRODUCT_VARIANT=A
```

Para la variante completa, usa:

```env
PRODUCT_VARIANT=B
```

Después de cada cambio, detén y vuelve a iniciar el servidor Django. No se deben editar manualmente `ENABLE_REPORTS` ni `ENABLE_NOTIFICATIONS`: ambos valores se derivan de la variante elegida.

## Gestión técnica de las variantes

1. `config_product.py` mantiene los puntos de variación en diccionarios declarativos y centralizados.
2. `settings.py` valida la variante seleccionada y transforma esa configuración en banderas Django.
3. `doctor/urls.py` registra la aplicación `reports` únicamente si `ENABLE_REPORTS` es verdadero.
4. La plantilla de pacientes muestra el botón de exportación únicamente cuando la misma bandera está activa.
5. La vista CSV mantiene una comprobación adicional de la bandera; así, una ruta publicada por error no expone la funcionalidad cuando la variante la deshabilita.

Este enfoque corresponde a **configuración externa + banderas de características**: las aplicaciones permanecen reutilizables y la composición final se define al iniciar el producto.

## Capturas para el entregable

1. Selecciona `PRODUCT_VARIANT=A`, inicia sesión y captura el listado de pacientes: no debe aparecer **Exportar reporte CSV**.
2. Selecciona `PRODUCT_VARIANT=B`, reinicia el servidor y captura exactamente la misma vista: debe aparecer **Exportar reporte CSV**.

Como comprobación adicional, con la variante B la URL `/reports/patients/csv/` descarga el reporte; con la A, no está registrada y devuelve 404.
