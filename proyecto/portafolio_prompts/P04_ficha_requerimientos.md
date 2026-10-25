# P04 — Ficha de requerimientos arquitectónicos (semana 7)

## Objetivo
Convertir el texto libre de un cliente en una ficha preliminar estructurada de uso, superficie, ventilación, iluminación, normativa aplicable e información faltante. En el proyecto integrador «Sistema de IA para estimación de costos y presupuestos de construcción», esta ficha alimenta la recopilación de datos previos a presupuestar; no representa por sí sola una cuantificación ni un permiso válido.

## Fecha, modelo y versión
- Fecha: 2026-10-24.
- Modelo de referencia: ChatGPT (GPT-6 declarado en sesión).
- Temperatura no controlada.
- Técnica seleccionada: versión 4 (rol + contexto + formato + ejemplo).
- Prompt y guía: [plantilla_prompt_v1.md](../../laboratorios/semana07/plantilla_prompt_v1.md).

## Tabla resumida de iteraciones de demostración
| Iteración | Técnica acumulada | C1 | C2 | C3 | Total /18 |
|---|---|---:|---:|---:|---:|
| 0 | Zero-shot | 4 | 1 | 2 | 7 |
| 1 | Rol | 5 | 1 | 3 | 9 |
| 2 | Rol + contexto | 6 | 1 | 4 | 11 |
| 3 | Anterior + formato | 6 | 5 | 4 | 15 |
| 4 | Anterior + ejemplo | 6 | 6 | 5 | 17 |
| 5 | Anterior + sección Análisis | 6 | 3 | 6 | 15 |

**Robustez:** 6/6 con la entrada cuatro, no utilizada para diseñar la plantilla. La iteración 5 mejoró C3 pero perdió precisión de formato, por lo que se conserva la versión 4.

## Variables y limitaciones
Variables: `{ROL_LECTOR}`, `{TIPO_ESPACIO}`, `{UBICACION}`, `{CAMPOS}`, `{ENTRADA}`.

Si un dato falta se marca NO ESPECIFICADO; si contradice otro, CONTRADICTORIO. Nunca deben asumirse normativa aplicable, presupuesto, superficie construible o autorizaciones. Se requiere contraste con archivos del proyecto y normativa oficial.

## Evidencia y transparencia
Se utilizaron respuestas documentales de demostración con una rúbrica común. **No** se verificaron 18 conversaciones nuevas aisladas ni capturas auténticas; por tanto, los puntajes son ilustrativos y se refieren a las respuestas archivadas, no a una prueba empírica independiente.

Archivos de la semana: [laboratorios/semana07](../../laboratorios/semana07/).
