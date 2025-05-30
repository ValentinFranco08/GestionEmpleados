from . import db
from .empleado import Empleado

class Gerente(Empleado):
    __tablename__ = 'gerentes'
    id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True)
    departamento = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'gerente',
    }

    def trabajar(self):
        return f"{self.nombre} está gestionando el departamento de {self.departamento}."
