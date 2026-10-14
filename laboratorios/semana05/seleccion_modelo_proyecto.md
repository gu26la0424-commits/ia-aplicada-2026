# Selección de modelo generativo para el proyecto Sistema de IA para estimación de costos y presupuestos de construcción

## Modelos evaluados
La comparativa de Semana 1 contiene ChatGPT, Gemini y DeepSeek, pero sus respuestas siguen pendientes. No constituye una evaluación completada. En Semana 5 se midió el texto con tiktoken 0.14.0, codificación o200k_base. Un tokenizador no es un modelo generativo evaluado. AI Studio devolvió 502 y la prueba alternativa en ChatGPT no produjo una respuesta completa.

## Evidencia de tokens
Documento de referencia: 1473 tokens. Documento con aguja: 1489 tokens. Párrafo español: 5.84 caracteres por token; inglés: 5.75. El documento está paginado en cuatro páginas de referencia. La hoja resultados_experimentos.xlsx contiene los conteos medidos. Los tokens de Gemini pueden ser distintos.

## Evidencia de temperatura
No hay ejecuciones válidas para comparar. Temperatura de precisión propuesta: 0, si el modelo elegido permite configurarla. Temperatura creativa propuesta: 0.7 como punto de partida, a validar frente a 1.5. Son hipótesis de configuración, no conclusiones experimentales. En la alternativa de ChatGPT se debe registrar “por defecto (desconocida)” y realizar nueve ejecuciones base más tres literales y tres creativas.

## Evidencia de contexto
Umbral de fallo: no medido. Los documentos de prueba contienen 1489 tokens en o200k_base. Los escenarios de 1, 2, 4 y 8 copias tienen 1489, 2962, 5908, 11800 tokens de texto, respectivamente; estas son mediciones de entrada, no ejecuciones del modelo. Una ventana hipotética de 32000 tokens permite aproximadamente 86.9 páginas antes de reservar instrucciones y salida. No demuestra recuperación correcta.

## Decisión
Herramienta propuesta provisionalmente: ChatGPT para organizar conceptos y detectar información faltante, con fórmulas externas para calcular cantidades y costos. Modelo/version final: pendiente de pruebas. En la interfaz no se verificó una versión ni el control numérico de temperatura. Si se utiliza una API configurable, empezar con 0 para extracción y 0.7 para ideas; validar precisión y variabilidad antes de adoptarlas.

No ingresar nombres, correos, ubicaciones exactas, rótulos o metadatos identificables que no sean necesarios, según la política de Semana 4. Utilizar documentos ficticios en las pruebas. No automatizar compras ni aprobación de presupuestos sin revisión humana.

## Estado de las evidencias
Conteos completados. Respuestas de temperatura, saturación, posición de aguja y sus capturas: pendientes de ejecución. No se afirma un límite de contexto ni una superioridad entre modelos sin datos.
