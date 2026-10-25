# Iteración 5: Anterior más análisis

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

Antes de la tabla escribe una sección titulada Análisis con tres viñetas: información explícita, inferencia segura y aspectos no determinables. Esta sección es la única excepción a la exigencia de tabla sin texto adicional. Después conserva exactamente la tabla.

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

**Análisis**
- Explícito: sala para dos, 4 × 5 m, ventana norte y LED.
- Inferencia segura: 20 m².
- No determinable: disposición municipal aplicable.

| Campo | Valor |
|---|---|
| Uso | Sala de lectura privada |
| Superficie | 20 m² |
| Ventilación | Ventana al patio norte |
| Iluminación | Natural y LED |
| Normativa aplicable | NO ESPECIFICADO |
| Información faltante | Normativa municipal y uso autorizado |

**Puntaje:** C1=2/2; C2=1/2; C3=2/2; total=5/6.

## Entrada 2

**Texto original:**

> Quiero adaptar una parte de la planta baja de mi casa como consultorio de orientación psicológica.
> Necesito que se sienta tranquilo, con privacidad y espacio para conversar.
> Me gustaría que entrara bastante luz natural.
> No sé cuántos metros cuadrados tengo disponibles.
> No he revisado cómo ventilarlo ni sé si se permiten consultas en mi domicilio.
> Tampoco he indicado el municipio donde está la casa.

**Respuesta de muestra:**

**Análisis**
- Explícito: consultorio de orientación en planta baja, privacidad y luz natural deseada.
- Inferencia segura: comprobar viabilidad del uso antes de adaptar.
- No determinable: metros disponibles, ventilación, municipio y permiso.

| Campo | Valor |
|---|---|
| Uso | Consultorio de orientación psicológica |
| Superficie | NO ESPECIFICADO |
| Ventilación | NO ESPECIFICADO |
| Iluminación | Luz natural deseada; solución NO ESPECIFICADO |
| Normativa aplicable | NO ESPECIFICADO |
| Información faltante | Superficie, ventilación, municipio, uso permitido y reglamento |

**Puntaje:** C1=2/2; C2=1/2; C3=2/2; total=5/6.

## Entrada 3

**Texto original:**

> Queremos un taller de maquetas para diez estudiantes en un local de la Ciudad de México.
> Un plano indica 6 m por 4 m, pero otro documento dice que el área es de 32 m².
> El cliente pide que el espacio no tenga ventanas por seguridad.
> En otra parte del encargo solicita ventilación cruzada abriendo ventanas.
> Se necesita mucha iluminación natural, aunque también se pide cerrar los muros exteriores.
> No conocemos la alcaldía, la ubicación precisa ni el uso de suelo autorizado.

**Respuesta de muestra:**

**Análisis**
- Explícito: diez estudiantes, 6 × 4 m y una cifra alternativa de 32 m².
- Inferencia segura: las dimensiones producen 24 m², en contradicción.
- No determinable: área correcta, ventanas y solución de luz, alcaldía y permisos.

| Campo | Valor |
|---|---|
| Uso | Taller de maquetas para diez estudiantes |
| Superficie | CONTRADICTORIO: 24 frente a 32 m² |
| Ventilación | CONTRADICTORIO: ventanas prohibidas y solicitadas |
| Iluminación | CONTRADICTORIO: luz natural y muros cerrados |
| Normativa aplicable | NO ESPECIFICADO |
| Información faltante | Confirmar área, ventilación, iluminación, alcaldía y uso permitido |

**Puntaje:** C1=2/2; C2=1/2; C3=2/2; total=5/6.

**Total de iteración:** 15/18.
