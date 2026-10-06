# Transformaciones y errores detectados — Semana 3

## Tabla de transformaciones

| Columna original | Qué se hizo | Técnica | Por qué |
| --- | --- | --- | --- |
| id | Conservar | Sin transformación | Se necesita para referencia del registro, pero no identifica por sí solo a la persona. |
| nombre | Seudonimizar | Código estable P001, P002... | Permite agrupar accesos de una misma persona sin exponer su nombre. |
| correo | Eliminar | Eliminación | No es necesario para detectar patrones de acceso. |
| telefono | Eliminar | Eliminación | No es necesario para detectar patrones de acceso. |
| fecha_acceso | Generalizar | Semana del año | Reduce precisión temporal y mantiene tendencias. |
| hora_entrada | Generalizar | Franja horaria | Reduce precisión y conserva patrones de horario. |
| area | Conservar | Sin transformación | Es necesaria para analizar dónde ocurren los accesos. |
| empresa | Generalizar | tipo_empresa | Reduce la identificación indirecta por organización. |
| motivo | Conservar | Sin transformación | Aporta contexto al patrón y no identifica por sí solo. |


## Errores introducidos contra detectados

| Tipo de error | Introducidos | Detectados | Faltaron | Por qué |
| --- | --- | --- | --- | --- |
| Fila duplicada exacta | 2 | 2 | 0 | La herramienta de duplicados debe detectarlos si se seleccionan correctamente todas las columnas excepto id. |
| Fecha en formato distinto | 3 | 3 | 0 | El formato puede normalizarse al convertir las fechas a un formato único. |
| Fecha inválida | 1 | 1 | 0 | El mes 13 no corresponde a una fecha válida y debe marcarse como incidencia. |
| Correo sin dominio o con mayúsculas | 3 | 3 | 0 | Las mayúsculas se normalizan; el correo sin dominio queda como inválido. |
| Teléfono con espacios o menos de diez dígitos | 3 | 3 | 0 | Los espacios se eliminan; los teléfonos incompletos quedan como incidencia. |
| Área con distinta capitalización | 3 | 3 | 0 | NOMPROPIO y ESPACIOS permiten normalizar la categoría. |
| Celda vacía en empresa o teléfono | 3 | 3 | 0 | La validación de vacíos permite localizar las incidencias. |
| Hora fuera de horario laboral | 3 | 3 | 0 | La validación las identifica, pero no las corrige porque pueden ser accesos reales. |


## Criterios aplicados

- Los duplicados se eliminaron comparando todas las columnas excepto `id`.
- El correo se normaliza a minúsculas y se valida, pero se elimina del archivo anonimizado.
- El teléfono se valida, pero se elimina del archivo anonimizado.
- La fecha se generaliza al número de semana del año.
- La hora se generaliza a `Madrugada`, `Mañana`, `Tarde` o `Noche`.
- El área se conserva con capitalización normalizada.
- La empresa se generaliza a `Constructora`, `Diseño` o `Soporte TI`.
- El nombre se sustituye por un identificador estable `P001`, `P002`, etc.
- La tabla privada que relaciona nombres con seudónimos no se sube al repositorio.

## Nota
Todos los datos del laboratorio son ficticios. `accesos_limpio` y la tabla de seudónimos se mantienen fuera del repositorio, como indican las instrucciones.
