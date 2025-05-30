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
        empleado.nombre = request.form['nombre']
        empleado.salario = float(request.form['salario'])
        tipo = request.form['tipo']

        # Cambiar el tipo de empleado si es necesario
        if tipo == 'desarrollador' and empleado.tipo != 'desarrollador':
            nuevo = Desarrollador(id=empleado.id, nombre=empleado.nombre, salario=empleado.salario, lenguaje="Python")
            db.session.delete(empleado)
            db.session.add(nuevo)
            empleado = nuevo
        elif tipo == 'gerente' and empleado.tipo != 'gerente':
            nuevo = Gerente(id=empleado.id, nombre=empleado.nombre, salario=empleado.salario, departamento="Ventas")
            db.session.delete(empleado)
            db.session.add(nuevo)
            empleado = nuevo
        elif tipo == 'empleado' and empleado.tipo != 'empleado':
            nuevo = Empleado(id=empleado.id, nombre=empleado.nombre, salario=empleado.salario)
            db.session.delete(empleado)
            db.session.add(nuevo)
            empleado = nuevo

        empleado.nombre = request.form['nombre']
        empleado.salario = float(request.form['salario'])

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar.html', empleado=empleado)


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
