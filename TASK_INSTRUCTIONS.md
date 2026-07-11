# SESIÓN 1: Identificación de componentes reutilizables

**Actividad**:

1. Seleccionen el proyecto Django con el que van a trabajar.
2. Revisen el código e identifiquen:
  - Módulos o apps que podrían usarse en otros proyectos (por ejemplo: autenticación, gestión de usuarios, carga de archivos).
  - Funcionalidades opcionales (por ejemplo: panel administrativo, exportar a PDF, búsquedas avanzadas).

**Herramientas de apoyo**:
- Diagrama de arquitectura de carpetas del proyecto
- Hoja de análisis de funcionalidades

**Producto**:
- Tabla: componentes reutilizables vs. componentes específicos
- Diagrama de arquitectura funcional (puede ser realizado en draw.io o a mano)

--- 

# SESIÓN 2: Modularización y separación de variantes

**Actividad**:

1. Aíslen una funcionalidad opcional del proyecto (por ejemplo, exportar reportes).
2. Muévanla a una app Django independiente (si no lo está).
3. Implementen una bandera de configuración (por ejemplo, en settings.py) para activar o desactivar la funcionalidad.

**Python**:
- settings.py

```python
ENABLE_REPORTS = True
```

- views.py

```python
from django.conf import settings

if settings.ENABLE_REPORTS:
    # Mostrar opción de exportar
```

**Herramientas de apoyo**:
- settings.py
- if condicional en vistas/plantillas

**Producto**:
- App separada para funcionalidad opcional
- Captura de vista con/ sin la funcionalidad activada

---

# SESIÓN 3: Configuración de variabilidad

**Actividad**:

1. Simulen dos variantes del mismo producto:
  - Variante A: sistema básico sin funcionalidades extra.
  - Variante B: sistema completo con funcionalidades extendidas.
2. Cree un archivo config_product.py donde definan qué características tiene cada variante:

**python**

- config_product.py

```python
PRODUCT_A = {
 'ENABLE_REPORTS': False,
 'ENABLE_NOTIFICATIONS': False
}

PRODUCT_B = {
 'ENABLE_REPORTS': True,
 'ENABLE_NOTIFICATIONS': True
}
```

3. Usen esta configuración en settings.py o directamente en las vistas.

**Herramientas de apoyo**:
- Archivos de configuración
- include() condicional en urls.py

**Producto**:
- Dos capturas distintas del mismo sistema con variabilidad funcional
- Explicación técnica de cómo lograron gestionar variantes

---

# SESIÓN 4: Documentación y línea de productos

**Actividad guiada**:

1. Documenten el sistema como si formara parte de una línea de productos:
  - ¿Qué tienen en común todas las variantes?
  - ¿Qué cambia entre ellas?
  - ¿Qué patrón de reutilización usaron?
2. Elaboren un pequeño manual con:
  - Instrucciones para activar/desactivar características
  - Recomendaciones para reutilizar apps entre proyectos Django
3. Presenten su línea de productos con al menos:
  - Diagrama SPL (puede ser árbol de decisiones o modelo de características)
  - Tabla de variantes y configuración

**Producto**:
- Manual PDF: “Línea de productos basada en Django”
- Diagrama de variabilidad
- Capturas de interfaz por variante
