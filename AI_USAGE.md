# AI_USAGE.md — Registro de Uso de IA

> **Instrucciones:** Documentá las instancias **significativas** en que usaste IA
> (Cursor, Claude Code, Copilot, ChatGPT, etc.) para escribir código o tomar
> decisiones de diseño. Es un entregable obligatorio para ambos tracks. La defensa
> puede incluir preguntas sobre cualquier entrada de este registro.

---

## 🎯 Heurística: ¿cuándo SÍ documento, cuándo NO?

**Documentás cuando hubo una decisión, no cuando hubo un autocomplete.**

### ✅ Documentá si...

- Reescribiste el prompt **3 o más veces** hasta llegar al output correcto
- El output **requirió debugging** (no funcionó al primer intento)
- La IA propuso **un diseño que aceptaste sin haberlo pensado antes**
- **Rechazaste** una sugerencia por seguridad, performance o correctitud
- La IA **inventó** algo (Ghost Dependency, API obsoleta, lógica fantasma) y lo detectaste
- Usaste la IA para **refactorizar** un bloque complejo, no solo una línea
- Hiciste un **cambio arquitectónico** con asistencia de IA

### ⛔ No hace falta documentar si...

- La IA completó un `import` o un nombre de variable obvio
- Reescribió un docstring trivial
- Generó **boilerplate** que ya sabías que ibas a escribir igual
- Renombró una variable de forma mecánica
- Te sugirió un `for` o un `if` que cualquier autocompletado clásico (no IA) también hubiera sugerido

### 🧭 Regla de oro

> *Si dentro de 3 meses no vas a saber por qué tu código quedó así → documentalo.
> Si es obvio → no.*

**Cantidad esperada:** un proyecto del M5 típicamente genera entre **5 y 15 entradas** significativas. Si pasaste de 25, probablemente estás sobre-documentando. Si tenés menos de 3, probablemente estás sub-documentando.

---

## Resumen del proyecto

**Nombre del proyecto:**
**Estudiante/s:**

---

## Registro de decisiones asistidas por IA

### Entrada 001

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-09-08 |
| **Herramienta** | Gemini Antigravity |
| **Contexto** | Implementando el historial de transacciones. Partiendo de un enfoque TDD con tests fallidos para la validación y el endpoint de transacciones. |
| **Prompt exacto (o resumen)** | La IA implementó toda la funcionalidad base luego de indicarle que los tests fallaban. Esto incluyó refactors y corrección de tipado. |
| **Sugerencia de la IA** | La IA generó la funcionalidad completa: `historial_repo.py`, `historial_service.py` y `historial.py` (routers). Además, solucionó un conflicto de importación de `date` y corrigió múltiples errores de tipado estricto (mypy). |
| **Decisión tomada** | Aceptada sin modificaciones sustanciales, ya que el código pasaba los tests fallidos iniciales y cumplía con las validaciones estrictas. |
| **Impacto en el código** | Archivos: `app/repositories/historial_repo.py`, `app/routers/historial.py`, `app/schemas/transaction.py`, `app/services/historial_service.py` y `tests/test_transactions.py`. |

**Razonamiento en tus palabras:**
> Acepté la implementación porque la IA comprendió correctamente el requerimiento a partir de los tests fallidos. En lugar de limitarse a arreglar un error puntual, la IA estructuró correctamente las capas de repositorio, servicio y router, dejando un código limpio y que aprueba el escrutinio de mypy. Sin la IA, habría tenido que estructurar manualmente cada capa iterando sobre los errores de tipado e imports.

---

### Entrada 002

| Campo | Detalle |
|-------|---------|
| **Fecha** | YYYY-MM-DD |
| **Herramienta** | |
| **Contexto** | |
| **Prompt exacto (o resumen)** | |
| **Sugerencia de la IA** | |
| **Decisión tomada** | |
| **Impacto en el código** | |

**Razonamiento en tus palabras:**
>

---

<!-- Copia el bloque de "Entrada NNN" cuantas veces necesites -->

---

## Reflexión final

Responde al finalizar el proyecto (mínimo 100 palabras):

1. **¿En qué partes del proyecto la IA fue más útil?** ¿Por qué?

2. **¿En qué partes la IA generó código que tuviste que corregir?** Describe el error y cómo lo detectaste.

3. **¿Hubo alguna sugerencia de la IA que rechazaste completamente?** ¿Cuál fue tu razonamiento?

4. **¿Cómo cambió tu flujo de trabajo al usar IA vs no usarla?** ¿Fuiste más rápido? ¿Cometiste errores distintos?

5. **Completa esta frase:** "Como Agent Manager, el mayor riesgo de usar IA sin supervisión en este proyecto habría sido..."

