# Laboratorio — Mejora iterativa de prompts con métricas

**Estudiante:** Diego Axel Gómez Zúñiga · **Materia:** Inteligencia Artificial Aplicada · **Carrera:** Arquitectura · **Semana:** 7 · **Fecha:** 24/10/2026.

## Resumen
Se aplicó la misma evaluación a tres casos ficticios (completo, faltante y contradictorio) con seis variaciones de un prompt. La versión elegida fue la iteración 4 con 17/18 puntos en las muestras documentales. El caso de robustez obtuvo 6/6. No se simula que estas respuestas provengan de 18 chats independientes.

## Parte 1. Rúbrica

| Criterio | 0 puntos | 1 punto | 2 puntos |
|---|---|---|---|
| C1 Completitud | Faltan dos o más campos | Falta un campo | Están uso, superficie, ventilación, iluminación y normativa |
| C2 Formato | No sigue una tabla comparable | Tabla incompleta o tiene texto adicional | Exclusivamente tabla Campo/Valor con seis filas |
| C3 Incertidumbre | Inventa o resuelve contradicciones como certezas | Identifica algunos faltantes, pero agrega suposiciones | No inventa y marca NO ESPECIFICADO o CONTRADICTORIO |

**Por qué C3 importa:** si se da por hecho el área, la ventilación o una norma no comprobada, pueden producirse planos y presupuestos erróneos. Indicar qué debe medirse y verificarse reduce ese riesgo.

## Partes 2 y 3. Método
Se utilizaron sin cambios las tres entradas de `entradas.md`, y se añadió una sola técnica por iteración: rol, contexto, formato, ejemplo y análisis. En `iteracion_0.md` a `iteracion_5.md` figuran el prompt y tres respuestas íntegramente documentadas en cada caso.

## Parte 4. Resultados

| Iteración | Técnica | C1 | C2 | C3 | Total | Observación |
|---|---|---:|---:|---:|---:|---|
| 0 | Línea base (zero-shot) | 4 | 1 | 2 | 7 | Predomina prosa; la entrada incompleta recibe una superficie no informada. |
| 1 | Rol | 5 | 1 | 3 | 9 | El vocabulario técnico mejora, pero persisten supuestos y formatos variables. |
| 2 | Rol + contexto | 6 | 1 | 4 | 11 | Los campos se cubren; falta estandarizar la salida y controlar supuestos. |
| 3 | Rol + contexto + formato | 6 | 5 | 4 | 15 | La tabla eleva el formato; todavía aparecen recomendaciones mezcladas con datos. |
| 4 | Anterior + ejemplo (few-shot) | 6 | 6 | 5 | 17 | La plantilla queda uniforme; la entrada contradictoria conserva una sugerencia no solicitada. |
| 5 | Anterior + análisis previo | 6 | 3 | 6 | 15 | Mejor control de incertidumbre, pero el análisis previo incumple «solo tabla». |

**Mayor salto:** de iteración 2 a 3 (11 a 15; +4), principalmente por mejora en el formato (+4 en C2). **Caída:** iteración 5 respecto de 4 (17 a 15; −2), porque el análisis separado rompió la instrucción de únicamente tabla. **Decisión:** adoptar iteración 4 (17/18).

Decir "NO ESPECIFICADO" o "CONTRADICTORIO" es verificable, mientras que la orden general "no inventes" carece de una forma fija de presentar los faltantes.

**Robustez:** cuarto caso, biblioteca comunitaria de Guadalajara, 6/6. Promedio anterior: 17/3 = 5.67; diferencia = +0.33 puntos. Un caso nuevo examina si la salida funciona fuera de los ejemplos originales, pero no basta para garantizar validez general.

## Parte 5. Plantilla
La versión reutilizable está en `plantilla_prompt_v1.md`, con variables {ROL_LECTOR}, {TIPO_ESPACIO}, {UBICACION}, {CAMPOS} y {ENTRADA}. Incluye instrucciones de uso, modelo de referencia (GPT-6, ChatGPT), puntuación y limitaciones. El portafolio actualizado está en `portafolio_prompts.md` y en `laboratorios/semana06/portafolio_prompts.md`.

## Parte 6. Reflexión
1. Si quitara el ejemplo few-shot de la versión 4, volvería a la 3: de 17 a 15 puntos, una pérdida de **2** en las muestras. No conservaría el análisis previo de la 5, porque reduce dos puntos sin mejorar el total.
2. Para que dos personas obtengan las mismas notas se necesitan instrucciones literales de puntuación, respuestas íntegras, ejemplos de discrepancias y doble calificación independiente con resolución acordada.
3. Al cambiar de modelo siguen siendo válidas las entradas, los criterios, las variables y la metodología. Se deben volver a ejecutar y puntuar las seis versiones y documentar la configuración del nuevo modelo.

## Tablas del lunes y del miércoles
**Lunes 19 de octubre:** `comparacion_p01.md` contiene la tabla P01: registro A (144 palabras, bibliografía general) y B (150 palabras, referencias enlazadas); ambas citan dos NOM y un dato histórico de consumo. Se conservó como antecedente.
**Miércoles 21 de octubre:** texturas arquitectónicas: Fuentes válidas / Ejemplos / Procesos. Iteración 0: 1/2/1=4; iteración 1: 2/2/1=5; iteración 2: 2/2/2=6. Incluidas en Word.

## Declaración de IA y evidencias pendientes
ChatGPT ayudó a documentar pruebas de ejemplo, puntuar, redactar y preparar archivos. Las 18 respuestas son **demostrativas, no ejecuciones independientes verificadas**; faltan capturas auténticas de conversaciones nuevas, hoja de cálculo y carpeta de GitHub. No se inventan capturas.

## Referencias
Gómez Zúñiga, D. A. (2026, 19 de octubre). *Semana 7: Comparación de dos respuestas al P01* [Registro de clase]. https://github.com/gu26la0424-commits/ia-aplicada-2026/blob/main/laboratorios/semana07/comparacion_p01.md

Material de clase. (2026). *Laboratorio: mejora iterativa de prompts con métricas* [Guía del curso].
