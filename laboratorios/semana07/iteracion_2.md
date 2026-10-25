# Iteración 2: Rol y contexto

**Modelo de referencia:** GPT-6 (ChatGPT). Respuestas documentales de demostración, no sesiones independientes verificadas.

## Prompt aplicado con cada entrada

```text
Eres arquitecto responsable del levantamiento de requerimientos preliminares. Tu lector es el coordinador del proyecto, quien necesita datos claros y verificables.

Contexto: el texto viene de un cliente sin formación técnica. La ficha debe registrar seis filas: uso, superficie, ventilación, iluminación, normativa aplicable e información faltante. Solo confirma dimensiones y condiciones si están explícitas y no son contradictorias. No cites normas, coeficientes ni permisos sin verificación oficial.

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

Uso: sala de lectura para dos personas. Superficie: 20 m² (4 × 5 m). Ventilación: natural por ventana practicable. Iluminación: natural y LED. Normativa: verificación municipal pendiente; no se asigna clave sin consulta oficial. Falta confirmar normativa específica.

**Puntaje:** C1=2/2; C2=0/2; C3=2/2; total=4/6.

## Entrada 2

**Texto original:**

> Quiero adaptar una parte de la planta baja de mi casa como consultorio de orientación psicológica.
> Necesito que se sienta tranquilo, con privacidad y espacio para conversar.
> Me gustaría que entrara bastante luz natural.
> No sé cuántos metros cuadrados tengo disponibles.
> No he revisado cómo ventilarlo ni sé si se permiten consultas en mi domicilio.
> Tampoco he indicado el municipio donde está la casa.

**Respuesta de muestra:**

Uso: consultorio de orientación psicológica. Superficie: no indicada; se toma como referencia preliminar 18 m², sin confirmar. Ventilación: no determinada. Iluminación: natural, solicitada. Normativa: pendiente por desconocer municipio y permisos. Información faltante: dimensiones, ventanas, ubicación y uso autorizado.

**Puntaje:** C1=2/2; C2=0/2; C3=1/2; total=3/6.

## Entrada 3

**Texto original:**

> Queremos un taller de maquetas para diez estudiantes en un local de la Ciudad de México.
> Un plano indica 6 m por 4 m, pero otro documento dice que el área es de 32 m².
> El cliente pide que el espacio no tenga ventanas por seguridad.
> En otra parte del encargo solicita ventilación cruzada abriendo ventanas.
> Se necesita mucha iluminación natural, aunque también se pide cerrar los muros exteriores.
> No conocemos la alcaldía, la ubicación precisa ni el uso de suelo autorizado.

**Respuesta de muestra:**

La descripción tiene incompatibilidades y debe aclararse.

| Campo | Valor |
|---|---|
| Uso | Taller de maquetas |
| Superficie | 32 m² (aunque 6 × 4 = 24 m²) |
| Ventilación | Ventilación cruzada por ventanas |
| Iluminación | Natural |
| Normativa aplicable | Por verificar en CDMX |
| Información faltante | Alcaldía, ventanas, área real y uso permitido |

**Puntaje:** C1=2/2; C2=1/2; C3=1/2; total=4/6.

**Total de iteración:** 11/18.
