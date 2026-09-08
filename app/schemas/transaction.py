from typing import Optional
from decimal import Decimal
from datetime import date
from pydantic import BaseModel, Field

class TransactionQueryRequest(BaseModel):
    """
    Modelo de solicitud (request) para la consulta paginada del historial de transacciones.
    Basado en las HU 1 (Consulta paginada) y HU 2 (Filtrado básico) del PRD.
    """
    

    
    # POR QUÉ (date): Aseguramos que la entrada sea una fecha válida (YYYY-MM-DD).
    # Nota: La validación de que no supere los 90 días en el pasado corresponde
    # a las reglas de negocio (Service), por ende no se aplica aquí en el Schema.
    start_date: date = Field(
        ...,
        description="Fecha de inicio para el filtrado de transacciones."
    )
    
    # POR QUÉ (date): Aseguramos el formato correcto de fecha. 
    # La comparación entre start_date y end_date va en el Service (lógica de negocio).
    end_date: date = Field(
        ...,
        description="Fecha de fin para el filtrado de transacciones."
    )
    
    # POR QUÉ (pattern regex): Usamos una expresión regular para restringir 
    # los estados permitidos a valores fijos y seguros, rechazando cualquier 
    # otro string que no represente un estado válido en el sistema.
    status: Optional[str] = Field(
        default=None,
        pattern=r"^(Aprobada|Rechazada|Anulada)$",
        description="Filtro opcional para el estado de la transacción."
    )
    
    # POR QUÉ (gt=0): Una transacción válida en el sistema no puede tener un 
    # monto negativo ni igual a cero. Restringimos la entrada estructuralmente.
    amount: Optional[Decimal] = Field(
        default=None,
        gt=Decimal("0"),
        max_digits=12,
        decimal_places=2,
        description="Filtro opcional para coincidencia exacta de monto."
    )
    
    # POR QUÉ (ge=1): Protegemos la paginación garantizando que la página 
    # solicitada siempre sea 1 o mayor (evita páginas negativas o página 0).
    page: int = Field(
        default=1,
        ge=1,
        description="Número de página a consultar."
    )
    
    # POR QUÉ (ge=1, le=100): Cumplimos con el criterio de "sin sobrecargar el sistema",
    # forzando un límite mínimo de 1 y un máximo estricto de 100 registros por página.
    size: int = Field(
        default=50,
        ge=1,
        le=100,
        description="Cantidad de registros que se devolverán por página."
    )

class Transaction(BaseModel):
    """
    Entidad Transacción según el PRD.
    Representa un cobro o movimiento en la pasarela.
    Excluye datos completos de tarjeta y autenticación por seguridad.
    """
    id: str = Field(..., description="Identificador único de la transacción.")
    date: date = Field(..., description="Fecha en la que se realizó la transacción.")
    status: str = Field(
        ..., 
        description="Estado actual de la transacción (ej. Aprobada, Rechazada, Anulada)."
    )
    amount: Decimal = Field(
        ..., 
        max_digits=12, 
        decimal_places=2, 
        description="Monto de la transacción."
    )
    masked_card: Optional[str] = Field(
        default=None, 
        description="Datos parciales de la tarjeta (ej. enmascaramiento mostrando los últimos 4 dígitos)."
    )

class TransactionPaginatedResponse(BaseModel):
    """
    Modelo de respuesta para la consulta paginada de transacciones.
    """
    data: list[Transaction] = Field(..., description="Lista de transacciones en la página actual.")
    page: int = Field(..., description="Número de página actual.")
    size: int = Field(..., description="Cantidad de registros por página.")
    total_pages: int = Field(..., description="Cantidad total de páginas disponibles.")
    total_records: int = Field(..., description="Cantidad total de registros que coinciden con los filtros.")
