import pytest
from fastapi.testclient import TestClient
from datetime import date, timedelta

from app.main import app

client = TestClient(app)

def test_post_transactions_query_happy_path_201():
    """
    1. Happy Path (201): Consulta exitosa que cumple con todas las reglas y el PRD.
    """
    # Arrange
    # Calculamos fechas relativas al día de hoy para que el test sea determinístico y 
    # no falle por reglas de antigüedad (> 90 días) independientemente de cuándo se ejecute.
    today = date.today()
    start_dt = today - timedelta(days=15)
    
    payload = {
        "start_date": start_dt.isoformat(),
        "end_date": today.isoformat(),
        "status": "Aprobada",
        "amount": "150.00",
        "page": 1,
        "size": 50
    }

    # Act
    # Hacemos el POST al endpoint propuesto
    response = client.post("/transactions/query", json=payload)

    # Assert
    # Comportamiento esperado: La petición se acepta y crea/devuelve el recurso paginado (201)
    assert response.status_code == 201
    
    data = response.json()
    # Aseguramos que la estructura de la respuesta cumple el contrato paginado (TransactionPaginatedResponse)
    assert "data" in data
    assert isinstance(data["data"], list)
    assert "page" in data
    assert "total_pages" in data


def test_post_transactions_query_invalid_field_422():
    """
    2. Error 422: Enviar un Field inválido respecto a las reglas de Pydantic.
    En este caso, la página ('page') no puede ser menor a 1 (ge=1) y enviamos 0.
    """
    # Arrange
    today = date.today()
    payload = {
        "start_date": today.isoformat(),
        "end_date": today.isoformat(),
        "page": 0,  # <-- Invalido: rompe regla 'ge=1' de TransactionQueryRequest
        "size": 50
    }

    # Act
    response = client.post("/transactions/query", json=payload)

    # Assert
    # Comportamiento esperado: Pydantic intercepta la petición y FastApi devuelve 422
    assert response.status_code == 422
    
    response_data = response.json()
    assert "detail" in response_data
    
    # Comportamiento esperado: El error apunta específicamente al campo 'page'
    error_locs = [error["loc"] for error in response_data["detail"]]
    assert any("page" in loc for loc in error_locs)


def test_post_transactions_query_prd_edge_case_400():
    """
    3. Caso borde del PRD: Transacciones anteriores a 90 días.
    Según el PRD: "El sistema debe rechazar u omitir peticiones de transacciones anteriores a 90 días."
    Asumimos que el endpoint rechaza la petición como un Bad Request (400) por regla de negocio.
    """
    # Arrange
    today = date.today()
    # Generamos una fecha claramente superior a los 90 días permitidos
    start_dt_out_of_bounds = today - timedelta(days=120) 
    
    payload = {
        "start_date": start_dt_out_of_bounds.isoformat(),
        "end_date": today.isoformat(),
        "page": 1,
        "size": 50
    }

    # Act
    response = client.post("/transactions/query", json=payload)

    # Assert
    # Comportamiento esperado: El controlador / servicio rechaza la petición antes de procesarla (400)
    assert response.status_code == 400
    
    response_data = response.json()
    # Comportamiento esperado: El mensaje de error menciona la regla de negocio de los 90 días
    assert "90" in response_data.get("detail", "")
