from core.database import db

# class Paso:
#     def __init__(self, titulo, cuerpo, ingredientes):
#         self.titulo = titulo
#         self.cuerpo = cuerpo
#         self.ingredientes = ingredientes


class Paso(db.Model):
    __tablename__ = 'pasos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80))
    cuerpo = db.Column(db.String(500))

    ingredientes = db.relationship('Ingrediente', backref='paso')

    receta_id = db.Column(db.Integer, db.ForeignKey('recetas.id'))

    def __init__(self, titulo, cuerpo, receta_id):
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.receta_id = receta_id

    def __repr__(self):
        return f'<{self.id}:Paso {self.titulo}>'