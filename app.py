from flask import Flask, render_template, request, redirect, url_for, abort
from models import db, Empleado, Desarrollador, Gerente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empleados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    empleados = Empleado.query.all()
    return render_template('index.html', empleados=empleados)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        salario = float(request.form['salario'])
        tipo = request.form['tipo']

        if tipo == 'desarrollador':
            empleado = Desarrollador(nombre=nombre, salario=salario, lenguaje="Python")
        elif tipo == 'gerente':
            empleado = Gerente(nombre=nombre, salario=salario, departamento="Ventas")
        else:
            empleado = Empleado(nombre=nombre, salario=salario)

        db.session.add(empleado)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('agregar.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        salario = float(request.form['salario'])
        tipo = request.form['tipo']

        try:
            # Eliminar el objeto anterior
            db.session.delete(empleado)
            db.session.flush()  # Libera el ID para reusar

            # Crear una nueva instancia según el tipo seleccionado
            if tipo == 'desarrollador':
                nuevo = Desarrollador(id=id, nombre=nombre, salario=salario, lenguaje="Python")
            elif tipo == 'gerente':
                nuevo = Gerente(id=id, nombre=nombre, salario=salario, departamento="Ventas")
            else:  # tipo == 'empleado'
                nuevo = Empleado(id=id, nombre=nombre, salario=salario)

            db.session.add(nuevo)
            db.session.commit()
            return redirect(url_for('index'))

        except Exception as e:
            db.session.rollback()
            flash(f"Error al editar empleado: {str(e)}", "danger")
            return redirect(url_for('editar', id=id))

    return render_template('editar.html', empleado=empleado)



@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
