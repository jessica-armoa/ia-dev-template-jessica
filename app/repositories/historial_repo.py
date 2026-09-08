from datetime import date, timedelta
from typing import List, Dict, Any

class HistorialRepository:
    def __init__(self):
        # Fake in-memory: 5 transacciones fijas
        today = date.today()
        self.db = [
            {"id": "1", "date": today - timedelta(days=5), "status": "Aprobada", "amount": 150.00, "pan": "1234567890123456"},
            {"id": "2", "date": today - timedelta(days=10), "status": "Rechazada", "amount": 200.00, "pan": "9876543210987654"},
            {"id": "3", "date": today - timedelta(days=15), "status": "Aprobada", "amount": 300.00, "pan": "4567123456789012"},
            {"id": "4", "date": today - timedelta(days=20), "status": "Anulada", "amount": 50.00, "pan": "3456789012345678"},
            {"id": "5", "date": today - timedelta(days=95), "status": "Aprobada", "amount": 1000.00, "pan": "1111222233334444"},
        ]

    def get_all(self) -> List[Dict[str, Any]]:
        return self.db
