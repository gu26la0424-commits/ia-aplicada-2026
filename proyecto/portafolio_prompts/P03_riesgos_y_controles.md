# P03 — Riesgos y controles

## Objetivo
Identificar riesgos del sistema de presupuestos y ofrecer controles con cuatro normas/hechos comprobables.

## Modelo y configuración
- Modelo: ChatGPT (GPT-6 declarado en la sesión; versión no verificada por otra vía)
- Temperatura: por defecto (no controlada)
- Fecha de ejecución: 2026-10-18

## Prompt (versión v1)
```text
Para el proyecto «Sistema de IA para estimación de costos y presupuestos de construcción», redacta cinco riesgos de usar respuestas generativas en decisiones sobre inmuebles. Separa el riesgo, el dato que debe verificarse y una medida de control. Incluye al menos tres afirmaciones normativas verificables relacionadas con eficiencia energética de edificios mexicanos; no inventes costos, clientes ni direcciones.
```

## Resultado obtenido
```text
1. Norma habitacional: La NOM-020-ENER-2011 regula la envolvente de edificios para uso habitacional. Riesgo: citar una norma equivocada en el presupuesto. Control: cotejar clave, título y texto oficial.
2. Norma no residencial: La NOM-008-ENER-2001 trata la envolvente de edificios no residenciales. Riesgo: aplicar requisitos de otra categoría. Control: verificar el uso del proyecto.
3. Aislamiento: La NOM-018-ENER-2011 se refiere a características y métodos de prueba de aislantes térmicos para edificaciones. Riesgo: especificar productos con base en requisitos inexistentes. Control: consultar la versión oficial y la documentación técnica.
4. Actualización normativa: Una resolución publicada el 4 de octubre de 2016 modificó aspectos de la NOM-020-ENER-2011. Riesgo: trabajar con versiones anteriores sin revisar cambios. Control: comprobar modificaciones y vigencia.
5. Presupuesto: La IA puede generar cantidades o precios no sustentados. Control: utilizar datos ficticios en pruebas, conservar fuentes y exigir revisión del responsable de costos antes de autorizar compras.
```

## Verificación
| Afirmación verificable | Fuente primaria | Clasificación |
|---|---|---|
| La NOM-020-ENER-2011 corresponde a envolvente de vivienda. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| La NOM-008-ENER-2001 corresponde a envolvente no residencial. | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |
| La NOM-018-ENER-2011 regula aislantes térmicos. | https://platiica.economia.gob.mx/normalizacion/nom-018-ener-2011/ | Correcta |
| El 4 de octubre de 2016 se publicó modificación de NOM-020-ENER-2011. | https://sidof.segob.gob.mx/notas/5455514 | Correcta |

Tasa de error de esta respuesta: 0 % (4 afirmaciones).

## Evaluación
- Qué funcionó: Relaciona riesgos, fuentes y controles.
- Qué falló: No comprueba precios de proveedores.
- Qué cambiaré en la siguiente versión: Solicitar responsables, frecuencia de revisión y criterio de aceptación.

## Historial de versiones
| Versión | Fecha | Cambio realizado | Resultado del cambio |
|---|---|---|---|
| v1 | 2026-10-18 | Versión inicial | Afirmaciones comprobadas con fuentes públicas. |

## Datos usados
Confirmo que este prompt cumple la sección 5 de la política de datos del proyecto: sí, porque no se compartieron datos identificables de clientes; se usaron datos ficticios y normativa pública.
