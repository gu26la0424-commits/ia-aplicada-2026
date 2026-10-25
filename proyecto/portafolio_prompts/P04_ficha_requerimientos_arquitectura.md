# P04 — Plantilla de ficha de requerimientos arquitectónicos (v1)

## Variables
- {ROL_LECTOR}: persona que usará la ficha.
- {UBICACION}: municipio y estado confirmados o NO ESPECIFICADO.
- {TIPO_DE_PROYECTO}: uso general del proyecto.
- {ENTRADA}: descripción literal del cliente.

## Prompt reutilizable
```text
Eres arquitecto responsable de documentar requerimientos iniciales para {TIPO_DE_PROYECTO}. Tu lector es {ROL_LECTOR}.
Ubicación declarada del predio: {UBICACION}. Se trata de una ficha preliminar y no sustituye un levantamiento ni una verificación normativa.

Responde únicamente con esta tabla Markdown, sin texto adicional:
| Campo | Valor |
|---|---|
| Uso | |
| Superficie | |
| Ventilación | |
| Iluminación | |
| Normativa aplicable | |
| Información faltante o contradictoria | |
Si un dato no consta o está en conflicto, escribe "NO ESPECIFICADO" o "POR VERIFICAR"; no inventes medidas, condiciones existentes, municipio ni normativa. Escribe los pendientes en la última fila.

Ejemplo independiente:
Entrada: "Busco una bodega para archivos en una oficina. El cuarto mide 2 × 3 m. No tiene ventanas. No conozco las reglas locales."
Salida:
| Campo | Valor |
|---|---|
| Uso | Bodega de archivos |
| Superficie | 6 m² (2 × 3 m) |
| Ventilación | NO ESPECIFICADO; no hay ventanas y no se describe sistema alterno |
| Iluminación | NO ESPECIFICADO |
| Normativa aplicable | POR VERIFICAR con autoridad local según el sitio |
| Información faltante o contradictoria | Ubicación, ventilación disponible, iluminación y requisitos locales |

Texto del cliente:
{ENTRADA}
```

## Instrucciones y límites
Reemplazar cada variable con información confirmada; para ubicación desconocida usar NO ESPECIFICADO. Copiar el prompt entero y verificar normativa y medidas con fuentes oficiales y visita al sitio.

**Modelo de referencia:** ChatGPT, GPT-6 declarado en esta sesión; temperatura no controlada. **Fecha:** 24-10-2026.
**Resultado ilustrativo:** 18/18 puntos con tres casos y 6/6 en robustez. **Importante:** las 18 respuestas todavía no son un experimento de chats independientes.

## Histórico de iteraciones

| Iteración | Técnica | C1 máximo 6 | C2 máximo 6 | C3 máximo 6 | Total máximo 18 | Observación |
| 0 | Línea base (zero-shot) | 3 | 0 | 2 | 5 | Texto libre: faltan campos, se supusieron medidas y ventilación. |
| 1 | Rol | 4 | 0 | 3 | 7 | El rol mejora el vocabulario, pero el formato y varias suposiciones persisten. |
| 2 | Rol + contexto | 5 | 0 | 3 | 8 | El contexto enumera campos, pero no corrige todas las suposiciones. |
| 3 | Rol + contexto + formato | 6 | 6 | 5 | 17 | La tabla corrige el formato; el caso 3 aún presupone ventilación. |
| 4 | Anterior + ejemplo (few-shot) | 6 | 6 | 6 | 18 | El ejemplo estabiliza los valores y explicita incertidumbre. |
| 5 | Anterior + análisis previo | 6 | 3 | 6 | 15 | La sección de análisis mejora trazabilidad, pero viola «solo la tabla». |
