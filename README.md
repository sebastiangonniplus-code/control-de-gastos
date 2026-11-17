💰 API Rest de Gestión de Gastos (FastAPI)API RESTful desarrollada en Python utilizando FastAPI para la gestión y control de gastos personales mediante operaciones CRUD completas y persistencia en archivos JSON. Este proyecto forma parte de tu aprendizaje y práctica en el desarrollo backend.🚀 Características PrincipalesOperaciones CRUD completas: Creación, lectura, actualización y eliminación de registros financieros.Validación de datos: Implementación de modelos con Pydantic para asegurar la integridad de los datos de entrada y salida.Persistencia local: Almacenamiento automático de los datos en formato JSON (data/expenses.json).Documentación interactiva: Interfaz automática generada por FastAPI mediante Swagger UI (/docs).Frontend integrado: Compatible con una interfaz web estática construida con HTML5 y Bootstrap 5 para consumir la API de manera visual.🛠️ Tecnologías y Librerías UtilizadasPython 3.x (Lenguaje de programación principal)FastAPI (Framework web asíncrono de alto rendimiento)Uvicorn (Servidor ASGI para ejecutar la aplicación)Pydantic (Validación de datos basada en tipos de Python)Bootstrap 5 (Diseño y componentes del frontend)📂 Estructura del ProyectoPlaintexttercer-proyecto/
│
├── data/
│   └── expenses.json       # Almacenamiento local de los gastos
├── models/
│   └── expense.py          # Modelos y esquemas de Pydantic
├── services/
│   └── expense_manager.py  # Lógica de negocio y persistencia en JSON
├── main.py                 # Definición de rutas y endpoints de FastAPI
├── index.html              # Interfaz gráfica (Frontend)
├── script.js               # Lógica de consumo de API con JavaScript (Fetch)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
⚙️ Guía de Instalación y EjecuciónSigue estos pasos para clonar y poner en marcha el proyecto en tu entorno local:1. Clonar el repositorioBashgit clone https://github.com/tu-usuario/tu-repositorio.git
cd tercer-proyecto
2. Crear y activar el entorno virtualEn Git Bash / Linux / macOS:Bashpython -m venv venv
source venv/Scripts/activate
En CMD (Windows):DOSpython -m venv venv
venv\Scripts\activate.bat
3. Instalar las dependenciasBashpip install fastapi uvicorn pydantic
4. Ejecutar el servidor de desarrolloInicia Uvicorn apuntando al archivo principal con recarga automática:Bashpython -m uvicorn main:app --reload
El servidor se iniciará localmente en: [http://127.0.0.1:8000](http://127.0.0.1:8000)📖 Endpoints de la APIUna vez que el servidor esté en marcha, puedes acceder a la documentación interactiva en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI) para probar los siguientes endpoints:MétodoEndpointDescripciónGET/expensesRetorna la lista completa de todos los gastos registrados.POST/expensesCrea un nuevo gasto validando los campos requeridos.GET/expenses/{gasto_id}Busca y retorna un gasto específico según su ID.PUT/expenses/{gasto_id}Actualiza los datos de un gasto existente conservando su ID.DELETE/expenses/{gasto_id}Elimina un gasto del registro por su ID.💻 Uso del FrontendPuedes interactuar visualmente con el sistema abriendo el archivo index.html directamente en tu navegador web o sirviéndolo mediante una extensión como Live Server en tu editor de código. Asegúrate de tener la API corriendo en segundo plano con Uvicorn para que las peticiones se comuniquen correctamente.
.
