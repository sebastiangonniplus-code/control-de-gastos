const API_URL = "http://localhost:8000/expenses";

document.addEventListener("DOMContentLoaded", () => {
    obtenerGastos();

    document.getElementById("expense-form").addEventListener("submit", async (e) => {
        e.preventDefault();
        await guardarGasto();
    });
});

// 1. Listar todos los gastos (GET)
async function obtenerGastos() {
    try {
        const response = await fetch(API_URL);
        const gastos = await response.json();
        
        const tbody = document.getElementById("expenses-table-body");
        tbody.innerHTML = "";

        gastos.forEach(gasto => {
            tbody.innerHTML += `
                <tr>
                    <td><strong>#${gasto.id}</strong></td>
                    <td>${gasto.titulo}</td>
                    <td>$${gasto.cantidad.toFixed(2)}</td>
                    <td><span class="badge bg-secondary">${gasto.categoria}</span></td>
                    <td>${gasto.fecha}</td>
                    <td class="text-center">
                        <button class="btn btn-sm btn-outline-primary me-1" onclick="cargarParaEditar(${gasto.id}, '${gasto.titulo}', ${gasto.cantidad}, '${gasto.categoria}', '${gasto.fecha}')">✏️</button>
                        <button class="btn btn-sm btn-outline-danger" onclick="eliminarGasto(${gasto.id})">🗑️</button>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Error al cargar los gastos:", error);
    }
}

// 2. Crear o Actualizar Gasto (POST o PUT)
async function guardarGasto() {
    const id = document.getElementById("expense-id").value;
    const titulo = document.getElementById("titulo").value;
    const cantidad = parseFloat(document.getElementById("cantidad").value);
    const categoria = document.getElementById("categoria").value;
    const fecha = document.getElementById("fecha").value;

    const datosGasto = { titulo, cantidad, categoria, fecha };

    try {
        let response;
        if (id) {
            // PUT /expenses/{id}
            response = await fetch(`${API_URL}/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(datosGasto)
            });
        } else {
            // POST /expenses
            response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(datosGasto)
            });
        }

        if (response.ok) {
            resetForm();
            obtenerGastos();
        } else {
            alert("Hubo un error al procesar la solicitud.");
        }
    } catch (error) {
        console.error("Error en la petición:", error);
    }
}

// 3. Eliminar Gasto (DELETE)
async function eliminarGasto(id) {
    if (!confirm("¿Estás seguro de que deseas eliminar este gasto?")) return;

    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (response.ok) {
            obtenerGastos();
        } else {
            alert("No se pudo eliminar el gasto.");
        }
    } catch (error) {
        console.error("Error al eliminar:", error);
    }
}

// 4. Preparar formulario para editar
function cargarParaEditar(id, titulo, cantidad, categoria, fecha) {
    document.getElementById("expense-id").value = id;
    document.getElementById("titulo").value = titulo;
    document.getElementById("cantidad").value = cantidad;
    document.getElementById("categoria").value = categoria;
    document.getElementById("fecha").value = fecha;

    document.getElementById("form-title").innerText = "Editar Gasto";
    document.getElementById("btn-submit").innerText = "Actualizar Gasto";
    document.getElementById("btn-submit").className = "btn btn-primary w-100";
    document.getElementById("btn-cancel").classList.remove("d-none");
}

// 5. Resetear formulario
function resetForm() {
    document.getElementById("expense-form").reset();
    document.getElementById("expense-id").value = "";
    document.getElementById("form-title").innerText = "Nuevo Gasto";
    document.getElementById("btn-submit").innerText = "Guardar Gasto";
    document.getElementById("btn-submit").className = "btn btn-success w-100";
    document.getElementById("btn-cancel").classList.add("d-none");
}