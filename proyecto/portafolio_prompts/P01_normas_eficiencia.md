# P01 — Normas y eficiencia energética

## Objetivo
Generar afirmaciones verificables sobre normas de eficiencia energética mexicanas.

## Modelo y configuración
- Modelo: ChatGPT (GPT-6 declarado en la sesión; versión no verificada por otra vía)
- Temperatura: por defecto (no controlada)
- Fecha de ejecución: 2026-10-18

## Prompt (versión v1)
```text
Redacta un párrafo de 150 palabras sobre la regulación de eficiencia energética en edificios en México. Incluye: el nombre exacto de al menos dos normas oficiales mexicanas con su clave, el año de publicación de cada una, una cifra estadística sobre consumo energético en edificios con su fuente y dos referencias bibliográficas completas en formato APA 7.
```

## Resultado obtenido
```text
En México existe la NOM-020-ENER-2011. La NOM-020-ENER-2011 regula la envolvente de edificios para uso habitacional. Fue publicada en el Diario Oficial de la Federación el 9 de agosto de 2011. Su objetivo es limitar la ganancia de calor a través de la envolvente. Se aplica a edificios nuevos para uso habitacional y a ampliaciones de edificios existentes. También existe la NOM-008-ENER-2001. Esta norma regula la envolvente de edificios no residenciales. Su publicación en el DOF fue el 25 de abril de 2001. Según la Secretaría de Energía, las edificaciones representaban el 20 % del consumo nacional de energía en la estrategia federal publicada en 2020. Estos datos son relevantes para quienes diseñan, comparan y presupuestan inmuebles: una referencia normativa incorrecta puede cambiar requisitos técnicos. Antes de incorporar cifras o normas a un proyecto se debe verificar cada clave, fecha y alcance en documentos oficiales.

Referencias (APA 7):
Secretaría de Energía. (2011). Norma Oficial Mexicana NOM-020-ENER-2011, eficiencia energética en edificaciones: Envolvente de edificios para uso habitacional. Diario Oficial de la Federación.
Secretaría de Energía. (2001). Norma Oficial Mexicana NOM-008-ENER-2001, eficiencia energética en edificaciones: Envolvente de edificios no residenciales. Diario Oficial de la Federación.
```

## Verificación
| Afirmación verificable | Fuente primaria | Clasificación |
|---|---|---|
| En México existe la NOM-020-ENER-2011. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| La NOM-020-ENER-2011 regula la envolvente de edificios para uso habitacional. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| Fue publicada en el Diario Oficial de la Federación el 9 de agosto de 2011. | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| Su objetivo es limitar la ganancia de calor a través de la envolvente. | https://dof.gob.mx/nota_detalle_popup.php?codigo=5203931 | Correcta |
| Se aplica a edificios nuevos para uso habitacional | https://dof.gob.mx/nota_detalle_popup.php?codigo=5203931 | Correcta |
| y a ampliaciones de edificios existentes. | https://dof.gob.mx/nota_detalle_popup.php?codigo=5203931 | Correcta |
| También existe la NOM-008-ENER-2001. | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |
| Esta norma regula la envolvente de edificios no residenciales. | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |
| Su publicación en el DOF fue el 25 de abril de 2001. | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |
| las edificaciones representaban el 20 % del consumo nacional de energía en la estrategia federal publicada en 2020. | https://sidof.segob.gob.mx/notas/docFuente/5585823 | Correcta |
| Secretaría de Energía. (2011). Norma Oficial Mexicana NOM-020-ENER-2011 | https://dof.gob.mx/normasOficiales.php?codp=4459&view=si | Correcta |
| Secretaría de Energía. (2001). Norma Oficial Mexicana NOM-008-ENER-2001 | https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/ | Correcta |

Tasa de error de esta respuesta: 0 % (12 afirmaciones).

## Evaluación
- Qué funcionó: Dos NOM existentes, fechas y cifra trazables.
- Qué falló: La respuesta sin consultar fuentes podría inventar fechas y referencias.
- Qué cambiaré en la siguiente versión: Solicitar URL por afirmación y etiquetar cifras históricas.

## Historial de versiones
| Versión | Fecha | Cambio realizado | Resultado del cambio |
|---|---|---|---|
| v1 | 2026-10-18 | Versión inicial | Afirmaciones comprobadas con fuentes públicas. |

## Datos usados
Confirmo que este prompt cumple la sección 5 de la política de datos del proyecto: sí, porque no se compartieron datos identificables de clientes; se usaron datos ficticios y normativa pública.
