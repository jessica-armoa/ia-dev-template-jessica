"""evals/eval_agent.py — Golden Set del agente RAG del Proyecto Final."""

from __future__ import annotations

import os
import sys

# Agregar el directorio raíz al PYTHONPATH para que encuentre 'app'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI

from app.agent.loop import run_agent

CASES = [
    {
        "id": "rango-90-dias",
        "question": "¿cuál es el horizonte del historial?",
        "expected_substring": "90 días",
    },
    {
        "id": "pan-solo-ultimos-4",
        "question": "¿cómo es el enmascaramiento del PAN?",
        "expected_substring": "últimos 4",
    },
    {
        "id": "fuera-de-alcance",
        "question": "¿cuál es la capital de Francia?",
        "expected_substring": "Sin coincidencias",
    },
]

def evaluate() -> None:
    client = OpenAI(base_url="http://localhost:8001/v1", api_key="mock")
    passed = 0
    for case in CASES:
        result = run_agent(case["question"], client)
        ok = case["expected_substring"].lower() in str(result).lower()
        mark = "[PASS]" if ok else "[FAIL]"
        print(f"{mark} {case['id']}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(CASES)} casos pasaron")

if __name__ == "__main__":
    evaluate()
