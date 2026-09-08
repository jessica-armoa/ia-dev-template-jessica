from fastapi import APIRouter

from app.schemas.transaction import (
    TransactionPaginatedResponse,
    TransactionQueryRequest,
)
from app.services.historial_service import HistorialService

router = APIRouter()

# Nota: El test utiliza POST /transactions/query y envía JSON,
# por lo tanto mantenemos este verbo y ruta para que los tests pasen en verde.
@router.post("/transactions/query", response_model=TransactionPaginatedResponse, status_code=201)
def query_transactions(request: TransactionQueryRequest):
    """
    Endpoint para consulta paginada del historial de transacciones.
    Solo maneja HTTP (validaciones vía Pydantic y status codes).
    """
    service = HistorialService()
    return service.get_transactions(request)
