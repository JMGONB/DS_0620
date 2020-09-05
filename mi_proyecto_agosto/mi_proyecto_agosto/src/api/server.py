
import os,sys
import json
import pandas as pd
from flask import Flask,render_template,redirect,request,jsonify


# ----------------------
# $$$$$$$ SERVER $$$$$$$$
app = Flask(__name__)  #Inicializa el servidor

@app.route("/") 
def default():
    return "<h1>soy la ruta por defecto</h1>.<p>Añadir get_json?id= para obtener json</p>"

@app.route("/get_json", methods = ['GET'])
def get_json():
    token = None
    # Obtener ruta del archivo y almacenar en la variable
    settings_file = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "\\resources\\json\\output\\residentes_edad.json"
    # Carga el json desde el archivo 
    with open(settings_file, "r") as json_file_readed:
        field = json.load(json_file_readed)
    if 'id' in request.args:
        token = str(request.args['id'])
    if token == 'L51391909':
        return str(field)
    else:
        return "Error al introducir la clave. Prueba nuevamente"

def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # RUTA HASTA EL FICHERO JSON

    settings_file = os.path.dirname(__file__) + "\\..\\..\\src\\api\\settings.json"

    # ABRIR FICHERO EN MODO LECTURA Y CARGAR EN VARIABLE JSON READED

    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # CARGA DE VARIABLES SERVER RUNNING Y SI ES TRUE CARGUE RESTO DE VARIABLES.
    
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server." + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()
    


