# Iteración 4: Anterior más ejemplo few-shot

**Modelo de referencia:** GPT-6 (ChatGPT). Respuestas documentales de demostración, no sesiones independientes verificadas.

## Prompt aplicado con cada entrada

```text
Eres arquitecto responsable del levantamiento de requerimientos preliminares. Tu lector es el coordinador del proyecto, quien necesita datos claros y verificables.

Contexto: el texto viene de un cliente sin formación técnica. La ficha debe registrar seis filas: uso, superficie, ventilación, iluminación, normativa aplicable e información faltante. Solo confirma dimensiones y condiciones si están explícitas y no son contradictorias. No cites normas, coeficientes ni permisos sin verificación oficial.

Responde únicamente con esta tabla Markdown, sin introducción ni texto adicional:

| Campo | Valor |
|---|---|
| Uso | |
| Superficie | |
| Ventilación | |
| Iluminación | |
| Normativa aplicable | |
| Información faltante | |

Si falta información escribe NO ESPECIFICADO. Ante dos datos incompatibles escribe CONTRADICTORIO y aclara el conflicto en Información faltante. No inventes normas, valores ni autorizaciones.

Ejemplo de entrada (referencia de formato): «Se requiere una bodega de utilería de 3 m × 4 m (12 m²) en Tepic, Nayarit; no se informó de ventanas, luz artificial ni normativa». Ejemplo de salida:

| Campo | Valor |
|---|---|
| Uso | Bodega de utilería |
| Superficie | 12 m² |
| Ventilación | NO ESPECIFICADO |
| Iluminación | NO ESPECIFICADO |
| Normativa aplicable | NO ESPECIFICADO: verificar disposiciones municipales vigentes |
| Información faltante | Ventilación, iluminación y norma específica comprobada |

Haz la ficha de requerimientos de este espacio:

{ENTRADA}
```

## Entrada 1

**Texto original:**

> Necesito una sala de lectura privada para dos personas en una vivienda de Aguascalientes, Aguascalientes.
> El espacio disponible mide 4 m por 5 m, es decir, 20 m².
> La utilizaremos para leer, estudiar y guardar libros.
> Tendrá una ventana practicable hacia un patio orientado al norte.
> Queremos iluminación natural durante el día y luminarias LED de apoyo.
> Todavía no hemos revisado qué normativa municipal aplica.

**Respuesta de muestra:**

| Campo | Valor |
|---|---|
| Uso | Sala de lectura privada para dos personas |
| Superficie | 20 m² (4 × 5 m) |
| Ventilación | Ventana practicable hacia patio norte |
| Iluminación | Natural y LED de apoyo |
| Normativa aplicable | NO ESPECIFICADO: verificar disposiciones de Aguascalientes |
| Información faltante | Reglamento y uso permitido específicos |

**Puntaje:** C1=2/2; C2=2/2; C3=2/2; total=6/6.

## Entrada 2

**Texto original:**

> Quiero adaptar una parte de la planta baja de mi casa como consultorio de orientación psicológica.
> Necesito que se sienta tranquilo, con privacidad y espacio para conversar.
> Me gustaría que entrara bastante luz natural.
> No sé cuántos metros cuadrados tengo disponibles.
> No he revisado cómo ventilarlo ni sé si se permiten consultas en mi domicilio.
> Tampoco he indicado el municipio donde está la casa.

**Respuesta de muestra:**

| Campo | Valor |
|---|---|
| Uso | Consultorio de orientación psicológica en planta baja de vivienda |
| Superficie | NO ESPECIFICADO |
| Ventilación | NO ESPECIFICADO |
| Iluminación | Luz natural solicitada; solución concreta NO ESPECIFICADO |
| Normativa aplicable | NO ESPECIFICADO: verificar municipio, uso del suelo y reglamentación |
| Información faltante | Área disponible, ventilación, ventanas, municipio, viabilidad del consultorio |

**Puntaje:** C1=2/2; C2=2/2; C3=2/2; total=6/6.

## Entrada 3

**Texto original:**

> Queremos un taller de maquetas para diez estudiantes en un local de la Ciudad de México.
> Un plano indica 6 m por 4 m, pero otro documento dice que el área es de 32 m².
> El cliente pide que el espacio no tenga ventanas por seguridad.
> En otra parte del encargo solicita ventilación cruzada abriendo ventanas.
> Se necesita mucha iluminación natural, aunque también se pide cerrar los muros exteriores.
> No conocemos la alcaldía, la ubicación precisa ni el uso de suelo autorizado.

**Respuesta de muestra:**

| Campo | Valor |
|---|---|
| Uso | Taller de maquetas para diez estudiantes |
| Superficie | CONTRADICTORIO: 6 × 4 = 24 m² frente a 32 m² declarados |
| Ventilación | CONTRADICTORIO: sin ventanas vs. ventilación cruzada por ventanas |
| Iluminación | CONTRADICTORIO: luz natural vs. muros cerrados |
| Normativa aplicable | NO ESPECIFICADO: falta alcaldía y uso confirmado |
| Información faltante | Confirmar área, ventanas, luz, alcaldía y uso del suelo; preliminarmente considerar 24 m² |

**Puntaje:** C1=2/2; C2=2/2; C3=1/2; total=5/6.

**Total de iteración:** 17/18.
