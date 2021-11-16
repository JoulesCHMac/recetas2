from core import app
import os

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 8080))


# Severless
#  - Nos abstrae del servidor
#  - Nos ofrecen una plataforma para monitorear nuestra aplicación
# Desventajas
#   - No tenemos acceso al servidor
# Proveedores
#  - Heroku: Cuenta de estudiante
#  - Google Cloud: Prueba gratuita.
    
# foreground

# Docker