# Funciones de la API


from flask import Flask, render_template, redirect, request, jsonify 
import os,sys
import json

# ---------
#  FLASK
# --------


app = Flask(__name__)  #inicializa
@app.route("/") 
def default():
    return "<h1>soy la ruta por defecto</h1>.<p>Añadir get_json?id= para obtener json</p>"

@app.route("/get_json", methods = ['GET'])
def get_json():
    token = None
    # Obtener ruta del archivo y almacenar en la variable
    settings_file = os.path.dirname(__file__) + "\\..\\..\\resources\\json\\output\\residentes_edad.json"
    # Carga el json desde el archivo 
    with open(settings_file, "r") as json_file_readed:
        field = json.load(json_file_readed)
    if 'id' in request.args:
        token = str(request.args['id'])
    if token == 'L51391909':
        return field
    else:
        return "Error al introducir la clave. Prueba nuevamente"




def return_error():
    return "Error al introducir la clave. Prueba nuevamente"