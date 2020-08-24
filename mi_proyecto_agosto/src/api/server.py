# Group B api server @jalex-yestera

# ----------------------
# $$$$$$$ SERVER $$$$$$$$
# ----------------------

def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # RUTA HASTA EL FICHERO JSON
    settings_file = os.path.dirname(__file__) + "\\..\\..\\resources\\json\\input\\settings.json"
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
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()
