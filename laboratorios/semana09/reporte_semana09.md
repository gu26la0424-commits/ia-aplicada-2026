# Semana 09 — Tu primer agente con herramientas en Dify

**Alumno:** Axel Gomez  
**Materia:** Inteligencia Artificial Aplicada — Global University  
**Carrera:** Arquitectura  
**Fecha de documentación:** 7 de noviembre de 2026  
**Agente previamente publicado:** [ARQUIBOT](https://udify.app/chat/tnvJYkIXoLPbBZO3)

> **Trazabilidad:** Este reporte se basa en la guía `semana09_primer_agente_dify.md`, en la ficha inicial de la Semana 1, en la política de datos de la Semana 4 y en un reporte anterior del 4 de noviembre con capturas reales de ARQUIBOT. **No se afirma haber ejecutado ahora pruebas de Dify ni se inventan capturas ni cifras del clima.** El Word y PDF completos se entregaron por ChatGPT; este archivo es la copia Markdown de consulta.

## Parte 1 — Modelo sin búsqueda

### Paso 1. Pregunta de prueba
> ¿Cuál es la temperatura y la humedad en este momento en Guadalajara, Jalisco? Con esos datos, ¿hacia dónde recomiendas orientar las ventanas de una sala de lectura?

### Paso 2. Respuesta 1: modelo solo
Prompt de control: **Responde solo con lo que ya sabes, sin buscar en internet.**

**Respuesta de referencia:** No puedo conocer la temperatura ni la humedad exactas de este momento en Guadalajara sin consultar una fuente en tiempo real. Para una sala de lectura conviene iluminación uniforme, control del deslumbramiento y ventilación regulable. Ventanas hacia el norte pueden ofrecer luz difusa; las orientadas al este reciben sol matutino; el poniente requiere mayor control solar. La orientación depende del sitio, las sombras, los vientos y la época. No sería correcto inventar grados o humedad.

**Clasificación:** reconoce que no cuenta con datos actuales; ofrece información general. **Captura real de la conversación: pendiente.**

## Parte 2 — Construcción del agente

- **Paso 3:** Cuenta Dify utilizada en una ejecución anterior del 4 de noviembre de 2026.
- **Paso 4:** Capturas antiguas muestran Dify Agent Strategies instalado y DuckDuckGo disponible.
- **Paso 5:** La aplicación previa se llama **ARQUIBOT**. La guía actual solicita un nombre con el formato `agente-lab09-gomez`; cambio pendiente.
- **Paso 6:** Chatflow anterior documentado: **Inicio → Agent → Respuesta**.
- **Paso 7:** Estrategia **FunctionCalling**, modelo **gpt-4.1-mini-2025-04-14**, herramienta **DuckDuckGo Search** habilitada, entrada del nodo vinculada a `Inicio / query` y máximo **3 iteraciones** (según reporte anterior). La guía actual pide **Qwen**, por lo que esta parte todavía no coincide con el requisito.
- **Paso 8:** El nodo Respuesta está conectado con `Agent / text`.

### Instrucciones propuestas, no aplicadas todavía
```text
Eres ARQUIBOT, un asistente del proyecto Sistema de IA para estimación de costos de construcción. Ayudas a estudiantes de Arquitectura, arquitectos y responsables de presupuestos a consultar información útil para estimaciones preliminares de obra.

Reglas:
1. Si una pregunta necesita información actual, usa DuckDuckGo Search antes de responder.
2. Si utilizaste la herramienta, indica al final cuál usaste y qué buscaste.
3. No inventes temperatura, humedad, normas, cantidades, precios ni fuentes.
4. Ningún presupuesto o compra queda aprobado sin revisión humana.
5. No solicites ni compartas datos personales innecesarios.
6. Responde en español y en un máximo de 150 palabras.
```

## Parte 3 — Prueba y validación

**Paso 9. Respuesta 2:** Falta ejecutar exactamente la pregunta del paso 1 en Preview. Existe una prueba anterior de orientación de ventanas en Guadalajara, pero **no incluye temperatura ni humedad actuales**.

**Paso 10. Tabla de comprobación:** sin cifras inventadas. Cuando el agente responda, registrar su temperatura y humedad y compararlas con el SMN/CONAGUA o clima del teléfono, con hora y fecha.

| Dato del agente | Verificación independiente | Coincidencia |
|---|---|---|
| Temperatura: pendiente | Pendiente | No evaluable |
| Humedad relativa: pendiente | Pendiente | No evaluable |

## Parte 4 — Registro y pruebas de control

**Paso 11.** Existe una captura real de la prueba previa sobre tendencias arquitectónicas que muestra `CALL DDGO_SEARCH` en `ROUND 1`. **Consulta exacta y resultados de la herramienta:** no visibles en esa captura; no se puede afirmar coincidencia completa. Para esta guía hace falta el registro del clima.

**Paso 12.** Pregunta requerida: **¿Qué es la humedad relativa?** Respuesta conceptual de referencia: porcentaje de vapor de agua presente respecto al máximo que puede contener el aire a la misma temperatura. No requiere datos actuales. **Uso efectivo de herramienta:** pendiente de revisar en Logs.

**Paso 13.** Prueba requerida: cambiar temporalmente Instruction a **Responde la pregunta.**, reiniciar Preview, repetir pregunta y restaurar las instrucciones. **Resultado observado:** pendiente; no se inventan diferencias.

## Parte 5 — Componentes

| Pieza | Lugar del agente | Sin la pieza |
|---|---|---|
| Modelo | Selector del nodo Agent | No interpreta preguntas ni redacta |
| Instrucciones | Campo Instruction | Pierde reglas explícitas de búsqueda, fuentes y límites |
| Herramienta | Tool List / DuckDuckGo Search | No consulta datos actuales |
| Memoria | Memoria del agente; se reportó desactivada | No mantiene el contexto propio de la memoria del agente |
| Ciclo de decisión | FunctionCalling | No decide y ejecuta llamadas a herramientas |

### Paso 15: Avance 9
El archivo completo está en [`proyecto/avance09_agente.md`](../../proyecto/avance09_agente.md). Se fundamenta en la [ficha inicial](../../proyecto/ficha_inicial.md) y la [política de datos](../semana04/politica_datos_proyecto.md).

## Parte 6 — Reflexión final

1. **¿Cuál sería más peligrosa?** Una respuesta que presentara cifras climáticas inventadas como actuales, porque podría orientar mal una decisión de diseño. La captura previa de `CALL DDGO_SEARCH` acredita una búsqueda en otra prueba; falta verificar la prueba exacta.
2. **¿Qué nunca debe decidir solo?** Aprobar compras, contratos o presupuestos definitivos. Se exige confirmación de un arquitecto o responsable de costos, revisión de cantidades, fuentes y registro de autorización.
3. **¿Qué pasa si falla una dependencia?** Sin Dify no ejecuta el flujo; sin créditos el modelo no contesta; sin DuckDuckGo no debe afirmar que verificó datos recientes. Preocupa especialmente confundir una búsqueda fallida con información validada.

## Evidencias y pendientes

Se conservan **siete capturas reales previas** en el Word/PDF: instalación de plugin, DuckDuckGo, Chatflow, nodo Agent, prueba anterior sobre orientación, llamada `CALL DDGO_SEARCH` y publicación. No equivalen a las capturas faltantes del nuevo experimento.

**Pendientes verificables:** captura modelo solo; modelo Qwen; nombre con formato pedido; respuesta exacta del agente a la pregunta climática; dos cifras contrastadas; argumentos/resultados de la llamada climática; registro de la pregunta conceptual; prueba sin instrucciones.

## Declaración de uso de IA

ChatGPT apoyó la redacción, las tablas, la adaptación del avance y el ensamblaje de capturas recuperadas. No se fabricaron datos ni pruebas inexistentes. La evaluación y entrega final requieren revisión del alumno.

## Referencias

- Global University. (2026). *Laboratorio: Tu primer agente con herramientas en Dify* [Material de clase, Semana 9].
- Gomez, A. (2026). *Reporte de la Semana 1* [Trabajo de clase].
- Gomez, A. (2026). *Política de datos de la Semana 4* [Trabajo de clase].
- Gomez, A. (2026, 4 de noviembre). *Laboratorio 9: Arma tu agente. ARQUIBOT* [Reporte de práctica con capturas].
