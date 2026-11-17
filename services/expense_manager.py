import os
import json

class ManagerExpenses:
    # Modela el administrador financiero.
    
    def __init__(self, archivo: str = "data/expenses.json"):
        self.archivo = archivo
        self.crear_archivo_si_no_existe()
      
    def crear_archivo_si_no_existe(self):
        # Crea el archivo si no existe.
        os.makedirs("data/", exist_ok=True)
        if not os.path.exists("data/expenses.json"):
             with open(self.archivo, 'w', encoding='utf-8') as archivo_json:
                 json.dump([], archivo_json, ensure_ascii=False, indent=4)
                
    def cargar_datos(self):
        # Carga los datos dentro del json.
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo_json:
               lista_del_json = json.load(archivo_json)
               return lista_del_json
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar_Datos(self, gastos):
        # Guarda los datos en el json.
        with open(self.archivo, 'w', encoding='utf-8') as archivo_json:
             json.dump(gastos, archivo_json, indent=4, ensure_ascii=False)
                
    def agregar_gasto(self, nuevo_gasto):
        # Agrega un gasto al json
        datos_actuales = self.cargar_datos()
        if len(datos_actuales) == 0:
            ultimo_id = 1
        else:
            ultimo_id = datos_actuales[-1]['id'] + 1

        gasto_dict = nuevo_gasto.model_dump(mode='json') 
        gasto_dict['id'] = ultimo_id
        datos_actuales.append(gasto_dict)
        self.guardar_Datos(datos_actuales)
   
        return gasto_dict

    def obtener_datos(self):
        # Retorna todos los gastos almacenados.
        return self.cargar_datos()

    def obtener_gastos_por_id(self, gasto_id):
        # Obtiene cada gasto por su correspondiente id.
        datos = self.cargar_datos()
        for datitos in datos:
                if datitos['id'] == gasto_id:
                    return datitos
        return None

    def eliminar_gasto(self, gasto_id):
        # Elimina un gasto por su id.
        datos = self.cargar_datos()
        for datitos in datos:
            if datitos['id'] == gasto_id:
                datos.remove(datitos)
                self.guardar_Datos(datos)
                return True
        return None    

    def actualizar_gasto(self, gasto_id, nuevos_datos):
        # Actualiza un gasto existente por su ID.
        datos = self.cargar_datos()
        gasto_dict = nuevos_datos.model_dump(mode="json")

        for datitos in datos:
            if datitos['id'] == gasto_id:
                gasto_dict['id'] = gasto_id
                index = datos.index(datitos)
                datos[index] = gasto_dict
                self.guardar_Datos(datos)
                return gasto_dict

        return None