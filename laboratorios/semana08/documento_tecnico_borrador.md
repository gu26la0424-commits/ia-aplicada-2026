# Documento técnico preliminar — borrador sin editar
## 1. Introducción
El sistema de IA para estimación preliminar de costos de construcción apoyará a arquitectos y responsables de presupuesto en la revisión de información de obra. La solución combinará generación de texto y reglas de cálculo para producir resultados rápidos y confiables, sujetos a validación profesional.

## 2. Alcance
**Incluye:**
- Interpretación inicial de descripciones de proyecto y organización de conceptos de obra.
- Apoyo para calcular cantidades y asociarlas con precios unitarios disponibles.
- Elaboración y actualización de estimaciones preliminares cuando cambian datos del proyecto.
- Detección de posibles omisiones para revisión por personal autorizado.

**No incluye:**
- Sustituir al arquitecto o al responsable del presupuesto.
- Autorizar compras, contrataciones o montos definitivos sin revisión humana.
- Incorporar datos identificables a modelos externos sin los controles de la política del proyecto.

## 3. Requisitos funcionales
- **RF-1.** Recibirá descripciones y conceptos de obra suministrados por un usuario autorizado.
- **RF-2.** Organizará los conceptos de manera clara y eficiente.
- **RF-3.** Aplicará reglas de cálculo a cantidades y precios unitarios proporcionados.
- **RF-4.** Señalará posibles omisiones y permitirá revisión humana antes de utilizar la estimación.
- **RF-5.** Permitirá actualizar una estimación cuando cambie la información del proyecto. El formato de entrada es [DATO PENDIENTE].

## 4. Requisitos no funcionales
- **RNF-1.** Cuidará la privacidad de los datos de forma adecuada.
- **RNF-2.** Registrará accesos y revisiones de modo verificable. El plazo de conservación es [DATO PENDIENTE].
- **RNF-3.** El nivel de precisión admisible es [DATO PENDIENTE], por acordar antes del uso profesional.
