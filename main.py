from fastapi import FastAPI, HTTPException
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


@app.get("/expenses/{gasto_id}")
def obtener_id(gasto_id: int):

     id_obtenido = manager.obtener_gastos_por_id(gasto_id)

     if id_obtenido == None:
          raise HTTPException(status_code=404, detail="...")

     return id_obtenido


@app.delete("/expenses/{gasto_id}")
def eliminar_id(gasto_id: int):
    # Llamamos al método de tu manager
    resultado = manager.eliminar_gasto(gasto_id)

    # Si retorna None, el ID no existía
    if resultado is None:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")

    # Retornamos un diccionario JSON de éxito para el cliente
    return {"mensaje": "Gasto eliminado con éxito"}