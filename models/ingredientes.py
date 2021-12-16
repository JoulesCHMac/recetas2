from core.database import db

# class Ingrediente:
#     # nombre = Column(Strin)
#     def __init__(self, nombre, cantidad, vegano):
#         self.nombre = nombre
#         self.cantidad = cantidad
#         self.vegano = vegano

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    cantidad = db.Column(db.Integer)
    vegano = db.Column(db.Boolean)
    
    receta_id = db.Column(db.Integer, db.ForeignKey('recetas.id'))
    
    paso_id = db.Column(db.Integer, db.ForeignKey('pasos.id'))

    def __init__(self, nombre, cantidad, vegano, receta_id):
        self.nombre = nombre
        self.cantidad = cantidad
        self.vegano = vegano
        self.receta_id = receta_id
    
    def __repr__(self):
        return f'<{self.id}:Ingrediente {self.nombre}>' 
