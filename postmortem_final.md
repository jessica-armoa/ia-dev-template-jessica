# Postmortem · Proyecto Final Jessica · 2026-09-10

## Qué funcionó

- El buscador lexical (buscar_regla_prd) fue más que suficiente para este PRD porque era chico y específico.
- Hacer correcciones apoyándome en el CI local (mypy y ruff) me ahorró subidas fallidas al repositorio.
- Reescribir y ajustar las preguntas del Eval Set para que coincidan con la extracción de palabras clave del Mock LLM.

## Qué no funcionó

- Usar `except Exception` en Python ocultaba errores importantes, Ruff me obligó a arreglarlo a tiempo.
- Dejar correr herramientas sin revisar la compatibilidad en Windows me dio dolores de cabeza con caracteres raros (emojis).
- La configuración por defecto de `mypy` explotaba internamente por el código tan pesado de la librería de `openai`.

## Qué haría distinto

- Usar un LLM real o un modelo local más inteligente (como llama3) en vez de un mock tan duro.
- Configurar el PYTHONPATH o correr todo con módulos (`-m`) desde el día 1 para evitar los `ModuleNotFoundError`.

## 3 lecciones aprendidas

1. Sobre agentes: Si el "system prompt" no es clarísimo (las barandas), el agente se rompe fácil.
2. Sobre RAG: Un buscador de texto básico funciona perfecto si sabes exactamente qué palabras buscar.
3. Sobre trabajo con IA: Es mejor pedirle a la IA arreglos puntuales cuando un linter falla, que dejarla escribir un archivo de 500 líneas sola.
