from . import db
from .empleado import Empleado

class Desarrollador(Empleado):
    __tablename__ = 'desarrolladores'
    id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True)
    lenguaje = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'desarrollador',
    }

    def trabajar(self):
        return f"{self.nombre} está programando en {self.lenguaje}."
