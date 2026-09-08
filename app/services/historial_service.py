from datetime import date
from fastapi import HTTPException
from app.schemas.transaction import TransactionQueryRequest, TransactionPaginatedResponse, Transaction
from app.repositories.historial_repo import HistorialRepository

class HistorialService:
    def __init__(self):
        self.repo = HistorialRepository()

    def mask_pan(self, pan: str) -> str:
        """Regla de negocio: Enmascarar el PAN mostrando solo los últimos 4 dígitos."""
        return f"****{pan[-4:]}"

    def get_transactions(self, request: TransactionQueryRequest) -> TransactionPaginatedResponse:
        today = date.today()
        
        # Regla de negocio: No consultar > 90 días
        if (today - request.start_date).days > 90:
            raise HTTPException(
                status_code=400, 
                detail="No se pueden consultar transacciones con antigüedad mayor a 90 días."
            )
            
        all_txs = self.repo.get_all()
        
        filtered = []
        for tx in all_txs:
            # Filtro fecha
            if not (request.start_date <= tx["date"] <= request.end_date):
                continue
            # Filtro estado
            if request.status and tx["status"] != request.status:
                continue
            # Filtro monto
            if request.amount is not None and tx["amount"] != float(request.amount):
                continue
                
            filtered.append(tx)
            
        # Mapeo y enmascaramiento
        mapped = []
        for tx in filtered:
            mapped.append(Transaction(
                id=tx["id"],
                date=tx["date"],
                status=tx["status"],
                amount=tx["amount"],
                masked_card=self.mask_pan(tx["pan"])
            ))
            
        # Paginación
        total_records = len(mapped)
        total_pages = max(1, (total_records + request.size - 1) // request.size)
        
        start_idx = (request.page - 1) * request.size
        end_idx = start_idx + request.size
        
        paginated_data = mapped[start_idx:end_idx]
        
        return TransactionPaginatedResponse(
            data=paginated_data,
            page=request.page,
            size=request.size,
            total_pages=total_pages,
            total_records=total_records
        )
