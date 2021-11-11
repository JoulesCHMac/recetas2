class Receta:
    def __init__(self, id, nombre, dificultad, tiempo, descripcion, costo, calificacion, imagen):
        self.id = id
        self.nombre = nombre
        self.dificultad = dificultad
        self.tiempo = tiempo
        self.descripcion = descripcion
        self.costo = costo
        self.calificacion = calificacion
        self.imagen = imagen

        self.ingredientes = []
        self.pasos = []

    def agregar_paso(self, paso):
        self.pasos.append(paso)
        return self.pasos

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        return self.ingredientes

    def mostrar_pasos(self):
        return self.pasos

    def mostrar_ingredientes(self):
        return self.ingredientes
