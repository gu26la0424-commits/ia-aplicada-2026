# Laboratorio — Verificación de respuestas y portafolio de prompts

**Estudiante:** Diego Axel Gómez Zúñiga · **Carrera:** Arquitectura · **Semana:** 6 · **Fecha:** 18 de octubre de 2026.

**Proyecto:** Sistema de IA para estimación de costos y presupuestos de construcción.

## Propósito y método
Se descompusieron 24 afirmaciones y se compararon con documentos originales del DOF, el catálogo oficial de normas y CONUEE. Se usaron las categorías Correcta, Parcialmente correcta y Alucinada. Se construyeron archivos de reglas de verificación y portafolio P01–P03.

**Limitación:** Solo se ejecutó ChatGPT. El segundo texto es una muestra sintética con errores intencionales para practicar el protocolo; no se afirma una ejecución real de un segundo modelo.

## Prompt exacto (versión Arquitectura)
```text
Redacta un párrafo de 150 palabras sobre la regulación de eficiencia energética en edificios en México. Incluye: el nombre exacto de al menos dos normas oficiales mexicanas con su clave, el año de publicación de cada una, una cifra estadística sobre consumo energético en edificios con su fuente y dos referencias bibliográficas completas en formato APA 7.
```

## Respuesta íntegra de ChatGPT
```text
En México existe la NOM-020-ENER-2011. La NOM-020-ENER-2011 regula la envolvente de edificios para uso habitacional. Fue publicada en el Diario Oficial de la Federación el 9 de agosto de 2011. Su objetivo es limitar la ganancia de calor a través de la envolvente. Se aplica a edificios nuevos para uso habitacional y a ampliaciones de edificios existentes. También existe la NOM-008-ENER-2001. Esta norma regula la envolvente de edificios no residenciales. Su publicación en el DOF fue el 25 de abril de 2001. Según la Secretaría de Energía, las edificaciones representaban el 20 % del consumo nacional de energía en la estrategia federal publicada en 2020. Estos datos son relevantes para quienes diseñan, comparan y presupuestan inmuebles: una referencia normativa incorrecta puede cambiar requisitos técnicos. Antes de incorporar cifras o normas a un proyecto se debe verificar cada clave, fecha y alcance en documentos oficiales.

Referencias (APA 7):
Secretaría de Energía. (2011). Norma Oficial Mexicana NOM-020-ENER-2011, eficiencia energética en edificaciones: Envolvente de edificios para uso habitacional. Diario Oficial de la Federación.
Secretaría de Energía. (2001). Norma Oficial Mexicana NOM-008-ENER-2001, eficiencia energética en edificaciones: Envolvente de edificios no residenciales. Diario Oficial de la Federación.
```

## Texto sintético de contraste (NO Gemini, NO DeepSeek)
```text
La NOM-020-ENER-2011 fue publicada en 2012 y se aplica a edificios residenciales nuevos. La NOM-008-ENER-2001 se publicó en 2002 y regula inmuebles no residenciales. La NOM-018-ENER-2011 apareció en el DOF el 14 de diciembre de 2011. Establece características y métodos de prueba para aislantes térmicos destinados a edificaciones. Una estrategia federal de 2020 atribuye a las edificaciones el 25 % del consumo total de energía nacional. Un estudio difundido por la CONUEE en 2019 indicó que el consumo eléctrico de edificios no residenciales era casi el triple del calculado en el Balance Nacional de Energía. En 2016 se derogó la NOM-020-ENER-2011. En 2023 se publicó la NOM-099-ENER-2023 sobre edificios históricos. Estos datos podrían orientar decisiones preliminares de arquitectura, aunque deberían comprobarse en el Diario Oficial de la Federación y el catálogo de normas. Las referencias siguientes se incluyen como material de contraste del laboratorio.

Referencias (APA 7):
Secretaría de Energía. (2020). Estrategia de transición para promover el uso de tecnologías y combustibles más limpios. Diario Oficial de la Federación.
Secretaría de Energía. (2023). Norma Oficial Mexicana NOM-099-ENER-2023, eficiencia energética de edificios históricos. Diario Oficial de la Federación.
```

## Coincidencias y contradicciones
Ambos textos nombraron NOM-020-ENER-2011 y NOM-008-ENER-2001. Difieren en los años 2011/2012 y 2001/2002 y en la cifra de consumo 20 %/25 %. Tener una bibliografía con aspecto académico, incluso en dos textos coincidentes, no prueba su existencia sin consultar el registro primario.

## Protocolo de verificación
Para cada afirmación: descomponerla; buscar la clave, fecha o cifra en el documento oficial; registrar URL y resultado; clasificarla; calcular la tasa de error como (parciales + alucinadas) / total x 100. El archivo CSV tiene todas las filas y resultados.

## Resumen
| Corpus | Total | Correctas | Parcialmente correctas | Alucinadas | Error |
|---|---:|---:|---:|---:|---:|
| Modelo 1: ChatGPT | 12 | 12 | 0 | 0 | 0 % |
| Texto de contraste sintético | 12 | 6 | 3 | 3 | 50 % |
| Total del ejercicio | 24 | 18 | 3 | 3 | 25 % |

### Resumen por tipo
| Tipo | Total | Correctas | Parciales | Alucinadas | Error |
|---|---:|---:|---:|---:|---:|
| Fecha | 5 | 3 | 2 | 0 | 40 % |
| Cifra | 3 | 2 | 1 | 0 | 33.33 % |
| Norma o ley | 11 | 9 | 0 | 2 | 18.18 % |
| Referencia bibliográfica | 4 | 3 | 0 | 1 | 25 % |
| Otro | 1 | 1 | 0 | 0 | 0 % |

### Ejemplo correcto
La NOM-020-ENER-2011 fue publicada en el DOF el 9 de agosto de 2011. Fuente oficial: https://dof.gob.mx/normasOficiales.php?codp=4459&view=si. Resultado: **Correcta**.

### Ejemplo alucinado
La afirmación "En 2016 se derogó la NOM-020-ENER-2011" contradice la resolución oficial, que fue una **modificación** de la norma. Fuente: https://sidof.segob.gob.mx/notas/5455514. Resultado: **Alucinada**. La referencia ficticia "NOM-099-ENER-2023, eficiencia energética de edificios históricos" no aparece en la búsqueda realizada del catálogo. Su ausencia requiere todavía búsqueda manual de cinco minutos y captura para cerrar el requisito docente.

## Parte 3: Reglas
Ver [reglas_verificacion_proyecto.md](reglas_verificacion_proyecto.md). Se verificará la clave y fecha de cada NOM, el documento original de estadísticas y referencias, la vigencia real de normas, los cálculos del presupuesto y los datos personales antes de usar IA externa.

## Parte 4: Portafolio
Ver [índice de prompts](../../proyecto/portafolio_prompts/README.md). P01 contiene el prompt literal de esta semana; P02 reutiliza el de Semana 1 guardado en laboratorios/semana01/comparativa_modelos.md; P03 cubre riesgos actuales. Temperatura por defecto, no controlada, como indica la ficha de Semana 5.

## Preguntas de la actividad

**¿Por qué dos modelos que citan lo mismo no prueban que una referencia exista?** Porque podrían repetir un error similar; solo una búsqueda y lectura del documento primario lo confirma.

**¿Cómo distinguir una falla de búsqueda de una alucinación?** Buscar por clave y título, variantes, fecha y dependencia, contrastar el DOF con el catálogo de normas y conservar URL, fecha, captura y tiempo de búsqueda. Las búsquedas negativas de la norma ficticia son provisionales.

**¿Por qué se guarda el texto íntegro en el portafolio?** Para preservar contexto, omisiones, referencias y el resultado específico que necesita auditarse; almacenar solo el prompt impide rastrear la respuesta efectivamente generada.

**1. Categoría que más falló:** Fechas (2/5, 40 %). Las claves frecuentes pueden repetirse con más consistencia, mientras que una fecha puntual requiere consultar el documento primario. El contraste es sintético, por lo que esta tasa no mide el desempeño real de dos modelos.

**2. Apariencia de las alucinaciones:** Fechas y referencias incorrectas parecían profesionales. La política de datos debe complementarse con verificación factual y la protección de datos personales.

**3. Consecuencias para la inversión:** Una norma mal citada puede producir presupuestos o especificaciones deficientes. Las reglas 4 y 7 exigen vigencia oficial y revisión profesional antes de gastar dinero.

## Declaración de uso de IA
ChatGPT ayudó a redactar, estructurar y generar los archivos. Los datos se cotejaron con registros oficiales. La muestra sintética se marca como tal. No se han fabricado capturas de equipo ni se ha presentado un segundo modelo como ejecutado.

## Pendientes
- Ejecutar el mismo prompt realmente en Gemini o DeepSeek; sustituir el contraste y recalcular la tasa.
- Adjuntar capturas originales de ambas respuestas, hoja de afirmaciones, DOF, búsqueda negativa, reglas y portafolio renderizado.
- Confirmar mediante búsqueda de al menos cinco minutos los títulos ausentes.

## Referencias consultadas
- N20: https://dof.gob.mx/normasOficiales.php?codp=4459&view=si
- N20detail: https://dof.gob.mx/nota_detalle_popup.php?codigo=5203931
- N08: https://platiica.economia.gob.mx/normalizacion/nom-008-ener-2001/
- N18: https://platiica.economia.gob.mx/normalizacion/nom-018-ener-2011/
- ENERGIA: https://sidof.segob.gob.mx/notas/docFuente/5585823
- CONUEE: https://www.gob.mx/conuee/articulos/investigadores-de-lawrence-berkeley-national-laboratory-autores-del-cuaderno-numero-3-nuevo-ciclo-de-la-conuee?idiom=es
- RES: https://sidof.segob.gob.mx/notas/5455514
- CAT: https://platiica.economia.gob.mx/normalizacion/normas-oficiales-mexicanas/
