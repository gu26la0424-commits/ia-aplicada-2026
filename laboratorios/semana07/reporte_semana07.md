# Laboratorio — Mejora iterativa de prompts con métricas
**Estudiante:** Diego Axel Gómez Zúñiga · **Carrera:** Arquitectura · **Materia:** Inteligencia Artificial Aplicada · **Semana:** 7 · **Fecha:** 24/10/2026.

## Objetivo
Crear un prompt para fichas preliminares de espacios, registrar tres entradas de cliente y medir seis iteraciones de rol, contexto, tabla, ejemplo y análisis.

## Parte 1. Rúbrica reproducible
| Criterio | 0 puntos | 1 punto | 2 puntos |
|---|---|---|---|
| C1 Completitud | Faltan dos o más de uso/superficie/ventilación/iluminación/normativa | Falta un campo | Cinco campos presentes |
| C2 Formato | Sin tabla Markdown de dos columnas | Tabla incompleta o texto adicional | Solo tabla Campo/Valor con seis filas |
| C3 Incertidumbre | Inventa datos o resuelve contradicciones como hechos | Avisa faltantes pero supone otros | Marca NO ESPECIFICADO/POR VERIFICAR y no inventa |

**Importancia C3:** un área o condición normativa inventada podría llegar al plano y al presupuesto. Los marcadores explícitos evitan tratar como certeza aquello que todavía debe medirse o verificarse.

## Partes 2 y 3. Método y archivos
Cada versión añade una sola técnica respecto de la anterior; se conservaron entradas 1–3. Las tres salidas de cada versión se guardaron completas en iteracion_0.md a iteracion_5.md. **Las respuestas son muestras demostrativas de una sesión, no 18 chats independientes.**

## Parte 4. Resultados
| Iteración | Técnica | C1 máximo 6 | C2 máximo 6 | C3 máximo 6 | Total máximo 18 | Observación |
| 0 | Línea base (zero-shot) | 3 | 0 | 2 | 5 | Texto libre: faltan campos, se supusieron medidas y ventilación. |
| 1 | Rol | 4 | 0 | 3 | 7 | El rol mejora el vocabulario, pero el formato y varias suposiciones persisten. |
| 2 | Rol + contexto | 5 | 0 | 3 | 8 | El contexto enumera campos, pero no corrige todas las suposiciones. |
| 3 | Rol + contexto + formato | 6 | 6 | 5 | 17 | La tabla corrige el formato; el caso 3 aún presupone ventilación. |
| 4 | Anterior + ejemplo (few-shot) | 6 | 6 | 6 | 18 | El ejemplo estabiliza los valores y explicita incertidumbre. |
| 5 | Anterior + análisis previo | 6 | 3 | 6 | 15 | La sección de análisis mejora trazabilidad, pero viola «solo la tabla». |

**Mayor salto:** 2 a 3, de 8/18 a 17/18 (+9; principalmente C2 +6). **Caída:** de 4 a 5, de 18 a 15 porque la explicación sale antes de la tabla. **Versión elegida:** iteración 4, más sencilla y con máximo ilustrativo 18/18.

Pedir "no inventes" deja abierta la forma de indicar dudas; prescribir NO ESPECIFICADO, POR VERIFICAR y una fila de faltantes permite puntuar el comportamiento.

**Robustez:** entrada 4 de sala de lectura, 6/6 ilustrativo, promedio previo 6/6, diferencia 0. Evalúa un caso nuevo sin cambiar la plantilla, aunque un solo caso no garantiza generalización.

## Parte 5. Plantilla
Ver plantilla_prompt_v1.md. Variables: {ROL_LECTOR}, {UBICACION}, {TIPO_DE_PROYECTO}, {ENTRADA}. Referencia de modelo: ChatGPT GPT-6, parámetros no controlados.

## Parte 6. Reflexión
1. Quitaría el ejemplo de la versión elegida: en las muestras el total baja de 18 a 17, pérdida de 1 punto. No incluiría el análisis de la 5, pues además baja C2 tres puntos.
2. Haría pública una rúbrica con decisiones literales, textos íntegros y ejemplos de puntuación; dos evaluadores calificarían por separado y documentarían desacuerdos. Haría las ejecuciones con sesiones y configuración equivalentes.
3. Al actualizar el modelo servirían las entradas, el formato, las variables y la rúbrica, pero se debe volver a generar, guardar y puntuar todo.

## Tablas de clases anteriores
**Lunes 19/10:** P01 comparó registro A (144 palabras, referencias incompletas) y B (150 palabras, con URL); ambos nombraron NOM-020-ENER-2011 y NOM-008-ENER-2001. Fuente: comparacion_p01.md del mismo directorio.
**Miércoles 21/10:** texturas arquitectónicas: criterio Fuentes válidas / Ejemplos / Procesos. Iteración 0: 1/2/1=4; 1: 2/2/1=5; 2: 2/2/2=6.

## Declaración de uso de IA
ChatGPT ayudó a generar casos ficticios, prompts, salidas de demostración, rúbrica, Word y CSV. No se fabricaron capturas ni se afirma haber abierto chats nuevos para cada caso. Quedan pendientes capturas reales del equipo, las ejecuciones independientes y su verificación.

## Referencias
Gómez Zúñiga, D. A. (2026, 19 de octubre). *Semana 7: comparación de dos respuestas al P01* [Registro de curso]. https://github.com/gu26la0424-commits/ia-aplicada-2026/blob/main/laboratorios/semana07/comparacion_p01.md

Material de clase. (2026). *Laboratorio — Mejora iterativa de prompts con métricas* [Instrucción del curso].
