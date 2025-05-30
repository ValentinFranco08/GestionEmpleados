from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .empleado import Empleado
from .desarrollador import Desarrollador
from .gerente import Gerente
