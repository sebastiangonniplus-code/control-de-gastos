from fastapi import FastAPI
from services.expense_manager import ManagerExpenses
from models.expense import MovimientosFinancierosDeEntrada, DevolucionAlUsuario
app= FastAPI()
manager = ManagerExpenses()

@app.post("/expenses", response_model=DevolucionAlUsuario)
def crear_gasto(gasto: MovimientosFinancierosDeEntrada):
     #Crea un gasto en el sistema.
     nuevo_gasto_creado =  manager.agregar_gasto(gasto)
    
     return nuevo_gasto_creado
     

@app.get("/expenses", response_model=list[DevolucionAlUsuario])
def listar_gastos():
     return manager.cargar_datos()