# Bitácora y análisis de la semana 8

## 1. Documento
El proyecto se sustentó en la ficha real y en la política de datos de su repositorio. Se documentaron **tres correcciones** y **dos hallazgos de información pendiente**. Se conservaron tres marcas [DATO PENDIENTE] en v1.

## 2. Presentación
Se preparó un guion de siete diapositivas y una presentación independiente en PPTX/PDF. No se ha creado una presentación mediante Gamma ni capturado una corrección suya. **No se anotan errores de Gamma como observados.**

## 3. Flujo original del taller
No está disponible la exportación ni la tabla original de pruebas y capturas. Se registra **sin evidencia de vueltas**, en lugar de inventar fallas, módulos o mensajes. No se asigna «verde» a pasos que no se observaron.

## 4. Demostración local independiente
El código local usa un filtro sencillo de términos. Resultado registrado sin excepciones:
- Control 1: derrumbe/peligro → URGENTE (coincide).
- Control 2: corrección de concepto → NORMAL (coincide).
- Difícil 3: trabe con fisuras → NORMAL, esperado URGENTE (error silencioso).
- Difícil 4: «¡URGENTE!» para portada administrativa → URGENTE, esperado NORMAL (error silencioso).
- Difícil 5: viga agrietada → NORMAL, esperado URGENTE (error silencioso).
- Difícil 6: losa deformada + renombrar hoja → NORMAL, esperado URGENTE (error silencioso).
- Difícil 7: actualizar notas para mañana → NORMAL (coincide).

**Advertencia:** esta prueba local no demuestra nada sobre la ejecución o calidad del flujo de la plataforma exigido en el taller.

## 5. Preguntas y reflexiones
Es indispensable definir el resultado esperado **antes** de ejecutar para evitar ajustar a posteriori la expectativa. Dos casos acertados solo sustentan que esas dos entradas salieron bien; no generalizan fiabilidad.

Una pieza de automatización inexistente y una librería inventada son la misma clase de dependencia inexistente. Un flujo en verde informa sobre ejecución, no necesariamente sobre semántica. Para descubrir errores silenciosos hacen falta etiquetas independientes, revisión profesional, registros y evaluaciones continuas.

Eliminar «responde con una sola palabra» puede cambiar la salida de una etiqueta a una oración y romper el contrato con el siguiente paso. **No se ejecutó aquí la rotura original del taller; es su explicación conceptual.**

No automatizaría la aprobación final de presupuestos ni la evaluación final de seguridad estructural. La persona competente debe decidir.

## 6. Seguridad y licencias
Las cuatro respuestas de seguridad originales no están disponibles y deben pegarse literalmente, como pide la consigna. El PDF/PPTX fue diseñado con formas, sin imágenes externas. Para imágenes de Gamma se debe verificar licencia antes de uso comercial.

Dartmouth College (2025) indica reconocer el uso de IA cuando está permitido y seguir instrucciones del docente: https://policies.dartmouth.edu/policy/guidelines-using-generative-artificial-intelligence-genai-coursework

## 7. Evidencia faltante
Captura de auditoría; Gamma antes/después y PDF exportado realmente de Gamma; flujo original con 3 pasos en verde; 2 pruebas originales; error silencioso real con ejecución verde; 4 respuestas del taller; JSON de la plataforma exportado; tiempos efectivamente medidos.
