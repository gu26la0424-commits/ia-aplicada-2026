# P02 — Selección de IA para presupuestos

## Objetivo
Reejecutar el prompt literal de la Semana 1; respetar la decisión provisional documentada en Semana 5.

## Modelo y configuración
- Modelo: ChatGPT (GPT-6 declarado en la sesión; versión no verificada por otra vía)
- Temperatura: por defecto (no controlada)
- Fecha de ejecución: 2026-10-18

## Prompt (versión v1)
```text
Actúa como consultor en inteligencia artificial. Trabajo en arquitectura y tengo este problema: calcular cantidades de obra y actualizar costos a partir de planos y catálogos consume varias horas cada semana. Los errores pueden causar compras incorrectas, desperdicio y sobrecostos. Quiero una herramienta que ayude a generar y actualizar un presupuesto preliminar sin sustituir la revisión profesional.

Responde en español con esta estructura:

1. Qué tipo de IA (predictiva, generativa o agente) es más adecuado para este problema y por qué.
2. Qué datos se necesitarían y de dónde saldrían.
3. Un riesgo ético o de privacidad que debería considerarse.
4. Un primer paso concreto que podría hacer esta semana sin programar.

Limita la respuesta a 250 palabras.
```

## Resultado obtenido
```text
1. Tipo de IA: Recomiendo combinar IA generativa, para ordenar las descripciones de obra, con cálculos deterministas para cantidades por precios unitarios. La IA debe apoyar; una persona debe aprobar el presupuesto.
2. Datos: Se requieren planos con medidas, catálogo de conceptos, unidades, cantidades y precios verificables. Las reglas aplicables dependen del uso del inmueble: la NOM-020-ENER-2011 se refiere a la envolvente de edificios habitacionales; la NOM-008-ENER-2001, a la de edificios no residenciales. Ambas aparecen en documentos oficiales de la Secretaría de Energía.
3. Riesgo: Un modelo puede inventar precios, áreas o requisitos normativos y provocar sobrecostos. Para proteger la privacidad, los planos y expedientes compartidos con servicios externos deben revisarse para retirar nombres, correos y ubicaciones exactas innecesarias.
4. Primer paso: Crear una hoja con cinco conceptos ficticios y columnas de cantidad, unidad, precio unitario y subtotal. Revisar manualmente multiplicaciones, catálogos y fuentes antes de confiar en el resultado.
```

## Verificación
| Afirmación verificable | Fuente primaria | Clasificación |
|---|---|---|
| La NOM-020-ENER-2011 trata edificios habitacionales. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| La NOM-008-ENER-2001 trata edificios no residenciales. | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |
| Ambas normas fueron expedidas por la Secretaría de Energía. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |

Tasa de error de esta respuesta: 0 % (3 afirmaciones).

## Evaluación
- Qué funcionó: Distingue IA generativa y cálculos deterministas.
- Qué falló: No cotiza materiales ni sustituye la revisión.
- Qué cambiaré en la siguiente versión: Incluir incertidumbre y trazabilidad de cada costo.

## Historial de versiones
| Versión | Fecha | Cambio realizado | Resultado del cambio |
|---|---|---|---|
| v1 | 2026-10-18 | Versión inicial | Afirmaciones comprobadas con fuentes públicas. |

## Datos usados
Confirmo que este prompt cumple la sección 5 de la política de datos del proyecto: sí, porque no se compartieron datos identificables de clientes; se usaron datos ficticios y normativa pública.
