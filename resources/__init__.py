# Installed packages
from flask import render_template, request, redirect
import requests

# Built-in packages
import base64

# Local packages
from models import *
from utils import debug
from secret import imgbb

recetas = []  # 0
# receta1 = Receta(
#     id=0,
#     nombre='Tacos',
#     dificultad='Difícil',
#     tiempo='2hr',
#     descripcion='Descripción del artículo',
#     costo=400,
#     calificacion=5,
# )
# 1
# receta2 = Receta(
#     id=1,
#     nombre='Pasta',
#     dificultad='Normal',
#     tiempo='25min',
#     descripcion='Descripción del artículo',
#     costo=100,
#     calificacion=2,
# )
# recetas.append(receta1)
# recetas.append(receta2)


# 2


def index():
    return render_template('index.html', recetas=recetas)


def ver_receta(id):
    # TODO: Validar id
    id = min([len(recetas) - 1, int(id)])
    return render_template('big_card.html', receta=recetas[id])


def crear_receta():
    """
    Esta función se encarga de crear una receta nueva.
    """
    if request.method == 'GET':
        return render_template('crear_receta.html')

    data = request.form
    image = request.files['imagen']
    
    print(image)
    params = dict(
        key=imgbb.apikey,
        image=base64.b64encode(image.read())
    )
    response = requests.post('https://api.imgbb.com/1/upload', data=params)
    if response.status_code == 200:
        imagen_url = response.json()['data']['url']
    else:
        imagen_url = 'https://i.ibb.co/KbvpmT9/imagen-2021-10-25-212241.png'

    receta_aux = Receta(
        id=len(recetas),
        nombre=data['titulo'],
        dificultad=data['dificultad'],
        tiempo=data['tiempo'],
        descripcion='Lorem ipsum dolor amet',
        costo=data['costo'],
        calificacion=3,
        imagen=imagen_url
    )

    # Añadir ingredientes
    for key, value in data.items(): #[['ingrediente-1', '50gr de harina']]
        if 'ingrediente' in key:
            # print(key, value)
            ingrediente_aux = Ingrediente(
                nombre=value, 
                cantidad=value.split()[0],
                vegano=False
            )
            receta_aux.agregar_ingrediente(ingrediente_aux)

    recetas.append(receta_aux)
    # TODO: Añadir pasos
    return redirect(f'/ver_receta/{receta_aux.id}')
