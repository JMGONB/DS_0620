# Función genérica para abrir, crear, leer  y escribir archivos
import pandas as pd 
import urllib
# Función para abrir el dataset. Esto pasa el archivo CSV (separado por comas) y transformo en un DataFrame
def read_open(name):    
    csv_df=pd.read_csv(name,sep=";")
    return csv_df
  
# Función para leer url

def read_url(url):
    url_def=urllib.request.urlopen(url)
    return url_def

# Función para leer url_2
def url_read(url_2):
    url_2_def=urllib.request.urlopen(url_2)
    return url_2_def

# Función para leer url_3
def open_url(url_3):
    url_3_def=urllib.request.urlopen(url_3)
    return url_3_def


