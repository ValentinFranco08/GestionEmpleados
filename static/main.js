document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-empleado");
    const lista = document.getElementById("lista-empleados");

    function cargarEmpleados() {
        fetch('/empleados')
            .then(res => res.json())
            .then(data => {
                lista.innerHTML = '';
                data.forEach(emp => {
                    const li = document.createElement('li');
                    li.textContent = `${emp.nombre} (${emp.tipo}) - $${emp.salario}`;
                    lista.appendChild(li);
                });
            });
    }

    form.addEventListener("submit", e => {
        e.preventDefault();
        const datos = new FormData(form);
        fetch('/empleados', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: datos.get('nombre'),
                tipo: datos.get('tipo')
            })
        })
        .then(res => res.json())
        .then(() => {
            form.reset();
            cargarEmpleados();
        });
    });

    cargarEmpleados();
});