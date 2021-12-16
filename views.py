from core import app
import resources

# Arquitectura vista controlador
app.route('/')(resources.index)

app.route('/ver_receta/<id>')(resources.ver_receta)

app.route('/crear', methods=["POST", "GET"])(resources.crear_receta)
