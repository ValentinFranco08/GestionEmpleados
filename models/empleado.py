from . import db

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_on': tipo,
        'polymorphic_identity': 'empleado'
    }

    def trabajar(self):
        return f"{self.nombre} está trabajando."
