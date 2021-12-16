from flask_sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)

from models import (ingredientes, pasos, recetas)

print(ingredientes.Ingrediente)

db.create_all()