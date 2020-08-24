# Funciones de la API
from flask import Flask
import request
# ---------
#  FLASK
# --------
app=Flask(__name__)  
@app.route("/")  
def default():
    return "soy la ruta por defecto. Añadir get_token?id=conseguir token,get_json?id=conseguir json"

@app.route("/get_token", methods = ['GET'])
def get_token():
    clave = None
    key = {"token": "L51391909"}
    if 'id' in request.args: 
        clave = str(request.args['id'])
    if clave == 'L345':
        return key['token']
    else:
        return "Error al introducir la clave. Prueba nuevamente"

@app.route("/get_json", methods = ['GET'])
def get_json():
    token = None
    # Obtener ruta del archivo
    settings_file = os.path.dirname(__file__) + "\\..\\..\\resources\\json\\output\\residentes_edad.json"
    # Carga el json desde el archivo 
    with open(settings_file, "r") as json_file_readed:
        field = json.load(json_file_readed)
    if 'id' in request.args:
        token = str(request.args['id'])
    if token == 'L51391909':
        return field