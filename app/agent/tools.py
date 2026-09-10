import os

PRD_PATH = "docs/prd/PRD.md"

def buscar_regla_prd(termino: str) -> str:
    """
    Busca lexicalmente el término en docs/prd/PRD.md y devuelve las coincidencias
    con ±3 líneas de contexto. Máximo 3 hits.
    """
    if not os.path.exists(PRD_PATH):
        return "Error: El archivo PRD no existe."

    termino_lower = termino.lower()
    coincidencias: list[str] = []

    try:
        with open(PRD_PATH, encoding="utf-8") as f:
            lineas = f.readlines()

        for i, linea in enumerate(lineas):
            if termino_lower in linea.lower():
                inicio = max(0, i - 3)
                fin = min(len(lineas), i + 4)
                contexto = "".join(lineas[inicio:fin]).strip()
                coincidencias.append(f"--- Hit {len(coincidencias) + 1} ---\n{contexto}")

                if len(coincidencias) >= 3:
                    break

        if not coincidencias:
            return f"Sin coincidencias para el término '{termino}'."

        return "\n\n".join(coincidencias)

    except OSError as e:
        return f"Error al leer el PRD: {str(e)}"

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "buscar_regla_prd",
            "description": "Busca un término exacto o parcial en el PRD (Product Requirements Document) y devuelve fragmentos de texto con contexto.",
            "parameters": {
                "type": "object",
                "properties": {
                    "termino": {
                        "type": "string",
                        "description": "Término de búsqueda relacionado con las reglas de negocio del Historial de Transacciones."
                    }
                },
                "required": ["termino"]
            }
        }
    }
]
