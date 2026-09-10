import json

from openai import OpenAI, OpenAIError

from app.agent.logger import log_step
from app.agent.tools import buscar_regla_prd

MAX_STEPS = 5

SYSTEM_PROMPT = """Sos un agente RAG especializado en el Historial de Transacciones · LegacyPay.
Tu objetivo es responder consultas del usuario basándote ÚNICAMENTE en el PRD.
REGLAS ESTRICTAS:
1. Solo respondés sobre el PRD. Si te preguntan otra cosa decís 'fuera de alcance'.
2. NO ejecutás acciones destructivas.
3. NO inventás resultados ni información que no esté en el documento.

En cada iteración, debes decidir qué acción tomar. DEBES responder ÚNICAMENTE con un objeto JSON válido con la siguiente estructura:
{
  "thought": "tu razonamiento interno sobre qué hacer a continuación",
  "action": "buscar_regla_prd" o "final",
  "action_input": {
    "termino": "término a buscar" // solo si action es buscar_regla_prd
  } // O bien, si action es final:
  // "action_input": {
  //   "respuesta": "tu respuesta final al usuario"
  // }
}

Herramientas disponibles:
- buscar_regla_prd: Busca lexicalmente un término en el PRD y devuelve contexto.
"""

def run_agent(query: str, client: OpenAI | None = None) -> str:
    """
    Ejecuta el ciclo ReAct procesando la consulta del usuario.
    """
    if client is None:
        client = OpenAI(
            base_url="http://localhost:8001/v1",
            api_key="mock"
        )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]

    for step in range(1, MAX_STEPS + 1):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0,
                response_format={"type": "json_object"}
            )

            content = response.choices[0].message.content
            if not content:
                return "Error: Respuesta vacía del LLM"

            decision = json.loads(content)
            messages.append({"role": "assistant", "content": content})

            action = decision.get("action")
            action_input = decision.get("action_input", {})

            if action == "final":
                respuesta = str(action_input.get("respuesta", str(action_input)))
                log_step(step, "final", action_input, respuesta)
                return respuesta

            elif action == "buscar_regla_prd":
                termino = action_input.get("termino", "")
                if not termino:
                    resultado = "Error: se requiere 'termino' en action_input"
                else:
                    resultado = buscar_regla_prd(termino)

                log_step(step, "buscar_regla_prd", action_input, resultado)
                messages.append({
                    "role": "user",
                    "content": f"Observation: {resultado}"
                })

            else:
                resultado = f"Error: acción desconocida '{action}'"
                log_step(step, action or "unknown", action_input, resultado)
                messages.append({
                    "role": "user",
                    "content": f"Observation: {resultado}"
                })

        except json.JSONDecodeError:
            resultado = "Error: El LLM no devolvió un JSON válido. Reintenta usando el formato correcto."
            log_step(step, "error_json", {}, resultado)
            messages.append({
                "role": "user",
                "content": f"Observation: {resultado}"
            })
        except OpenAIError as e:
            return f"Error en la ejecución del agente: {str(e)}"

    return "Error: Se alcanzó el número máximo de pasos (MAX_STEPS) sin respuesta final."

if __name__ == "__main__":
    # Prueba simple
    print(run_agent("¿Cuáles son los filtros permitidos?"))
