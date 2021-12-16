from core.database import db
# class Receta:
#     def __init__(self, id, nombre, dificultad, tiempo, descripcion, costo, calificacion, imagen):
#         self.id = id
#         self.nombre = nombre
#         self.dificultad = dificultad
#         self.tiempo = tiempo
#         self.descripcion = descripcion
#         self.costo = costo
#         self.calificacion = calificacion
#         self.imagen = imagen

#         self.ingredientes = []
#         self.pasos = []

#     def agregar_paso(self, paso):
#         self.pasos.append(paso)
#         return self.pasos

#     def agregar_ingrediente(self, ingrediente):
#         self.ingredientes.append(ingrediente)
#         return self.ingredientes

#     def mostrar_pasos(self):
#         return self.pasos

#     def mostrar_ingredientes(self):
#         return self.ingredientes

class Receta(db.Model):
    __tablename__ = 'recetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    dificultad = db.Column(db.String(80))
    tiempo = db.Column(db.String(80))
    descripcion = db.Column(db.String(500))
    costo = db.Column(db.String(80))
    calificacion = db.Column(db.String(80))
    imagen = db.Column(db.String(80))

    pasos = db.relationship('Paso', backref='receta')
    ingredientes = db.relationship('Ingrediente', backref='receta')

    def __init__(self, nombre, dificultad, tiempo, descripcion, costo, calificacion, imagen):
        self.nombre = nombre
        self.dificultad = dificultad
        self.tiempo = tiempo
        self.descripcion = descripcion
        self.costo = costo
        self.calificacion = calificacion
        self.imagen = imagen

    def __repr__(self):
        return f'<{self.id}:Receta {self.nombre}>'
