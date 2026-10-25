# Iteración 1: Rol

**Modelo de referencia:** GPT-6 (ChatGPT). Respuestas documentales de demostración, no sesiones independientes verificadas.

## Prompt aplicado con cada entrada

```text
Eres arquitecto responsable del levantamiento de requerimientos preliminares. Tu lector es el coordinador del proyecto, quien necesita datos claros y verificables.

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

Como arquitecto, registro: uso sala de lectura privada; 20 m² disponibles; ventilación natural por ventana al norte; iluminación natural y LED; norma municipal no identificada todavía. Es una ficha preliminar que debe validarse.

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

Uso: consultorio de orientación psicológica. Superficie: no se proporcionó, aunque 18 m² podrían ser suficientes. Ventilación: está pendiente de definir. Iluminación: natural solicitada. Falta confirmar ubicación y normativa aplicable.

**Puntaje:** C1=1/2; C2=0/2; C3=1/2; total=2/6.

## Entrada 3

**Texto original:**

> Queremos un taller de maquetas para diez estudiantes en un local de la Ciudad de México.
> Un plano indica 6 m por 4 m, pero otro documento dice que el área es de 32 m².
> El cliente pide que el espacio no tenga ventanas por seguridad.
> En otra parte del encargo solicita ventilación cruzada abriendo ventanas.
> Se necesita mucha iluminación natural, aunque también se pide cerrar los muros exteriores.
> No conocemos la alcaldía, la ubicación precisa ni el uso de suelo autorizado.

**Respuesta de muestra:**

Ficha del taller:

| Campo | Valor |
|---|---|
| Uso | Taller de maquetas, diez estudiantes |
| Superficie | 32 m² |
| Ventilación | Cruzada mediante ventanas |
| Iluminación | Natural abundante |
| Normativa aplicable | Normativa local de construcción por confirmar |
| Información faltante | Alcaldía y uso del suelo |

La propuesta se basa en la superficie indicada en el segundo documento.

**Puntaje:** C1=2/2; C2=1/2; C3=0/2; total=3/6.

**Total de iteración:** 9/18.
