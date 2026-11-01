# Documento técnico preliminar — versión revisada (v1)

## 1. Introducción
El proyecto propone apoyar a arquitectos, responsables de presupuestos y personal de obra en la preparación y actualización de estimaciones preliminares. Combina IA generativa para estructurar descripciones y conceptos con reglas de cálculo para cantidades y precios unitarios. Sus resultados son auxiliares: requieren revisión humana antes de cualquier decisión económica.

## 2. Alcance
**Incluye:**
- Organizar información textual de planos, catálogos y conceptos facilitados por usuarios autorizados.
- Aplicar reglas de cálculo a cantidades y precios unitarios aportados y mostrar los datos empleados.
- Generar estimaciones preliminares y actualizarlas cuando cambie la información de entrada.
- Marcar posibles omisiones y someterlas a revisión del responsable del presupuesto.

**No incluye:**
- Sustituir la validación técnica del arquitecto ni la revisión del responsable de costos.
- Aprobar compras, contrataciones o presupuestos definitivos de manera automática.
- Compartir nombres, correos, direcciones exactas o metadatos identificables con modelos externos cuando sean innecesarios.

## 3. Requisitos funcionales
- **RF-1.** Aceptar descripciones y conceptos de obra suministrados por un usuario autorizado.
- **RF-2.** Producir una lista de conceptos identificables y señalar los que estén incompletos o ambiguos para revisión.
- **RF-3.** Aplicar reglas explícitas a cantidades y precios unitarios proporcionados, sin inventar cifras ausentes.
- **RF-4.** Mostrar posibles omisiones y exigir validación humana antes de utilizar una estimación en decisiones económicas.
- **RF-5.** Actualizar el presupuesto preliminar cuando cambien las entradas; formatos admitidos: [DATO PENDIENTE].

## 4. Requisitos no funcionales
- **RNF-1.** Aplicar minimización y anonimización cuando sea posible; controlar accesos por roles, usar cifrado y MFA y revisar metadatos antes de consultar modelos externos.
- **RNF-2.** Mantener trazabilidad de accesos y revisiones; plazo específico de retención de registros: [DATO PENDIENTE].
- **RNF-3.** No presentar resultados como definitivos; tolerancia de error cuantitativo autorizada: [DATO PENDIENTE].

## Declaración de generación asistida
Modelo: ChatGPT, GPT-6 (OpenAI). Fecha: 31 de octubre de 2026. Prompt utilizado: `prompt_documento.txt` del expediente local y anexo A del reporte. Correcciones aplicadas: **3** frases vagas; se conservaron **3** marcas [DATO PENDIENTE]. Validación humana final del equipo: pendiente.
