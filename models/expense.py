from pydantic import BaseModel, Field
from datetime import date

class MovimientosFinancierosDeEntrada(BaseModel):
    #Modela los movimientos financieros introducidos.

    titulo: str
    cantidad: float= Field(...,gt=0)
    categoria: str
    fecha: date = Field(default_factory=date.today)


class DevolucionAlUsuario(MovimientosFinancierosDeEntrada):
    #Modela los datos retornados al usuario.
    id: int    