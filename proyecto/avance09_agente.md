# Avance 9 — Definición del agente del proyecto

**Proyecto:** Sistema de IA para estimación de costos de construcción  
**Prototipo conversacional:** ARQUIBOT  
**Alumno:** Axel Gomez — Arquitectura, Global University  
**Fecha:** 7 de noviembre de 2026

## 1. Objetivo

Ayudar a arquitectos y responsables de presupuestos a ordenar información de obra, estimar cantidades y producir presupuestos preliminares revisables; reducir omisiones y el tiempo de actualización sin sustituir la supervisión de una persona.

## 2. Qué recibe

- Preguntas escritas y descripciones de espacios.
- Superficies, dimensiones y cantidades proporcionadas por el equipo.
- Catálogos de conceptos y precios unitarios.
- **En etapas futuras:** planos, fotografías y documentos sujetos a revisión y anonimización. **No se declara que estas entradas documentales estén implementadas en ARQUIBOT.**

## 3. Qué hace por sí mismo

- Identifica conceptos de obra y organiza partidas.
- Solicita medidas o precios faltantes.
- Presenta cantidades y estimaciones como **borradores sujetos a verificación**.
- Marca posibles inconsistencias y cambios de datos.
- Busca referencias actualizadas cuando corresponde, identifica fuentes y comunica límites.

**(C) Acciones sujetas a confirmación humana:** aceptar cantidades finales, fijar costos unitarios definitivos, enviar presupuestos a clientes, autorizar compras o pagos y aprobar contrataciones. El agente no las ejecuta de forma autónoma.

## 4. Qué herramientas necesita

| Acción | Herramienta | Estado |
|---|---|---|
| Consultas actuales | DuckDuckGo Search | Documentada en Dify anterior |
| Interpretar preguntas | Modelo conversacional del nodo Agent | Documentado en Dify anterior |
| Leer catálogos y planos | Lector documental seguro | Propuesto |
| Calcular cantidades y aplicar precios | Motor de cálculos verificables | Propuesto |
| Crear presupuesto | Exportación a hoja de cálculo y PDF | Propuesto |
| Gestionar versiones y confirmaciones | Registro de cambios y autorización humana | Propuesto |

## 5. Lo que NO debe hacer

1. No inventar cantidades, precios, normas ni fuentes; marcar cualquier dato pendiente.
2. No convertir estimaciones preliminares en presupuestos definitivos sin revisión profesional.
3. No aprobar compras, pagos o contrataciones ni enviar documentos a terceros sin autorización explícita.
4. No compartir nombres, correos, ubicaciones exactas ni fotografías identificables sin necesidad legítima y controles.
5. No introducir a servicios externos de IA datos personales innecesarios; usar anonimización, minimización y revisión de metadatos.
6. No omitir riesgos o incertidumbres que puedan generar sobrecostos y desperdicios.

## Continuidad con Semanas 1 y 4

La [ficha inicial](ficha_inicial.md) plantea estimaciones y presupuestos preliminares para equipos de arquitectura, con validación humana antes de decisiones económicas. La [política de datos](../laboratorios/semana04/politica_datos_proyecto.md) exige minimización, control de acceso, seguridad, supervisión humana y evaluación de proveedores externos. Estos principios limitan al agente.

## Estado comprobado del prototipo

El reporte anterior documenta ARQUIBOT en Dify con Chatflow **Inicio → Agent → Respuesta**, estrategia **FunctionCalling**, modelo **gpt-4.1-mini-2025-04-14** y **DuckDuckGo Search**. El enlace publicado anteriormente es https://udify.app/chat/tnvJYkIXoLPbBZO3. Lectura de planos, cálculo y envío de presupuestos son capacidades **propuestas**, no funciones ya construidas.

## Uso de inteligencia artificial

ChatGPT colaboró en la estructura y redacción a partir de documentos propios del curso. Se diferenciaron las funciones realmente documentadas de las previstas. La evaluación final corresponde al estudiante.
