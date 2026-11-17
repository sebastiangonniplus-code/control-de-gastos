import os
import json

class ManagerExpenses:
    #Modela el administrador financiero.
    
    def __init__(self,archivo: str = "data/expenses.json"):
        self.archivo = archivo
        self.crear_archivo_si_no_existe()
      
    def crear_archivo_si_no_existe(self,):
        #Crea El archivo si no existe.

        os.makedirs("data/", exist_ok=True)
        if not os.path.exists("data/expenses.json"):
             with open(self.archivo,'w', encoding='utf-8') as archivo_json:
                 json.dump([],archivo_json, ensure_ascii=False, indent=4)
                
    def cargar_datos(self):
        #Carga los datos dentro del json.

        try:
            with open(self.archivo,'r', encoding='utf-8') as archivo_json:
               lista_del_json =json.load(archivo_json)
               return(lista_del_json)
        
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar_Datos(self,gastos):
        #Guarda los datos en el json.
        with open(self.archivo, 'w', encoding='utf-8') as archivo_json:
             json.dump(gastos,archivo_json,indent=4,ensure_ascii=False)
                
    def agregar_gasto(self,nuevo_gasto):
        #Agrega un gasto al json
        
        datos_actuales = self.cargar_datos()

        if len(datos_actuales) == 0:
            datos_actuales.append(1)

        else:
            ultimo_id = datos_actuales[-1]['id']
            datos_actuales.append['id'][ultimo_id + 1]  