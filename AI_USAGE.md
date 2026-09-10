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
| **Fecha** | 2026-09-09 |
| **Herramienta** | Gemini Antigravity |
| **Contexto** | Creación del esqueleto inicial de un agente RAG con el patrón ReAct para interactuar con el PRD. |
| **Prompt exacto (o resumen)** | Generar el esqueleto inicial del agente en Python 3.12 (tools, loop, logger) limitando los pasos a `MAX_STEPS = 5`, usando el prompt del sistema como baranda, e integrando un Mock LLM. |
| **Sugerencia de la IA** | La IA construyó `tools.py` para la búsqueda en el PRD, `logger.py` para registro en JSONL, y `loop.py` para el control de iteraciones ReAct utilizando un objeto JSON estructurado como salida. |
| **Decisión tomada** | Aceptada. Además, se hizo un ajuste posterior a la función `run_agent` para permitir la inyección de dependencias del cliente de OpenAI. |
| **Impacto en el código** | Archivos nuevos: `app/agent/tools.py`, `app/agent/logger.py`, `app/agent/loop.py`. |

**Razonamiento en tus palabras:**
> La IA fue clave para generar rápidamente la estructura *boilerplate* (herramienta de búsqueda léxica y esquema JSON) y armar el bucle principal de interacción ReAct que se comunica con el mock LLM respetando las reglas impuestas.

---

### Entrada 003

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-09-10 |
| **Herramienta** | Gemini Antigravity |
| **Contexto** | Arreglando errores del linter (Ruff) y tipado (Mypy). |
| **Prompt exacto (o resumen)** | "Tengo un error BLE001 en Ruff y un error de tipo en mypy." |
| **Sugerencia de la IA** | Cambió la excepción genérica a `OSError` y casteó la variable a string. |
| **Decisión tomada** | Aceptada para que el CI pase en verde. |
| **Impacto en el código** | Archivos `app/agent/tools.py` y `app/agent/loop.py`. |

**Razonamiento en tus palabras:**
> Usar excepciones generales es mala práctica. La IA encontró rápido las correctas.

---

### Entrada 004

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-09-10 |
| **Herramienta** | Gemini Antigravity |
| **Contexto** | Corriendo el script de evaluación. |
| **Prompt exacto (o resumen)** | "El comando me da ModuleNotFoundError." |
| **Sugerencia de la IA** | Agregó la ruta base a `sys.path` y cambió emojis a ASCII para la consola. |
| **Decisión tomada** | Aceptada. Permitió correr el test sin fallos en Windows. |
| **Impacto en el código** | Archivo `evals/eval_agent.py`. |

**Razonamiento en tus palabras:**
> Arreglos básicos de entorno para poder seguir probando el agente fácilmente.

---

### Entrada 005

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-09-10 |
| **Herramienta** | Gemini Antigravity |
| **Contexto** | Mejorando la tasa de éxito del Eval Set. |
| **Prompt exacto (o resumen)** | "Solo pasa 1 de 3 casos, ¿qué falta para que pasen más?" |
| **Sugerencia de la IA** | Ajustar las preguntas del test para que el Mock LLM encuentre la palabra clave correcta. |
| **Decisión tomada** | Aceptada. Pasaron 3/3 casos. |
| **Impacto en el código** | Archivo `evals/eval_agent.py`. |

**Razonamiento en tus palabras:**
> Fue útil entender cómo extrae palabras el mock. Cambiar la pregunta fue más rápido que reescribir el LLM falso.

---

## Reflexión final

Responde al finalizar el proyecto (mínimo 100 palabras):
1. **¿En qué partes del proyecto la IA fue más útil?** ¿Por qué?
> La IA fue particularmente útil para la estructuración rápida de la lógica de dominio (repositorios, servicios, routers) y para el diseño inicial del agente RAG. Al trabajar con esquemas y reglas predefinidas en el PRD, la IA pudo interpretar el contexto e implementar funciones completas (como el bucle ReAct, el JSON formatter de logs y la integración del Mock LLM) en minutos, resolviendo eficientemente la redacción del _boilerplate_.

2. **¿En qué partes la IA generó código que tuviste que corregir?** Describe el error y cómo lo detectaste.
> Generó código que requirió ajustes de arquitectura, como cuando el agente inicialmente no previó permitir la inyección de la dependencia del cliente de OpenAI, provocando fallos cuando quise probar el flujo con una instancia preexistente. Además, hubo fricción con el nivel de tipado estricto (no se anotaron los tipos en listas vacías generando advertencias de mypy) y el uso de `Exception` genérico que fue detectado y rechazado por el linter (Ruff BLE001). Todo se detectó al correr las comprobaciones obligatorias locales (`uv run ruff check` y `mypy`).

3. **¿Hubo alguna sugerencia de la IA que rechazaste completamente?** ¿Cuál fue tu razonamiento?
> Rechacé el uso de bloques genéricos `except Exception:` para atrapar fallos durante las llamadas al LLM y lectura de archivos. Razonamiento: Ocultar excepciones de forma general es una mala práctica de ingeniería que puede esconder problemas como `SyntaxError` o `KeyboardInterrupt`. Exigí que la captura fuera reemplazada explícitamente por `OSError` o `OpenAIError`.

4. **¿Cómo cambió tu flujo de trabajo al usar IA vs no usarla?** ¿Fuiste más rápido? ¿Cometiste errores distintos?
> Pasé de ser un "codificador de líneas" a un "auditor / gerente de agentes". Definitivamente la velocidad de producción aumentó enormemente (especialmente en la generación de la capa de API y las _tools_ del agente). Mis errores pasaron de ser "olvido de un punto y coma" a problemas semánticos y de compatibilidad de herramientas (conflictos con Ruff o versiones de Mypy), exigiendo que me vuelva más crítico al revisar el código antes de darle el visto bueno.

5. **Completa esta frase:** "Como Agent Manager, el mayor riesgo de usar IA sin supervisión en este proyecto habría sido..."
> "...permitir que el agente generara alucinaciones ('inventara' datos no contemplados) u omitiera validaciones, exponiendo potencialmente información confidencial del Historial de Transacciones y rompiendo el estricto aislamiento de datos exigido por el PRD ante la ausencia de _guardrails_ rigurosos."
