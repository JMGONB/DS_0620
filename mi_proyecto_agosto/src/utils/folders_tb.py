# Función genérica para abrir, crear, leer  y escribir archivos
import pandas as pd 
import urllib
from bs4 import BeautifulSoup

# Función para abrir el dataset. Esto pasa el archivo CSV (separado por comas) y transformo en un DataFrame
def read_open(name):    
    csv_df=pd.read_csv(name,sep=";")
    return csv_df
  
# Función para leer url

def read_url(url):
    html=urllib.request.urlopen(url)
    soup=BeautifulSoup( html,"html.parser")
    return soup

# Función para leer url_2

def url_read(url_2):
    html_2=urllib.request.urlopen(url_2)
    soup_6=BeautifulSoup(html_2,"html.parser")
    return soup_6

# Función para leer url_3

def open_url(url_3):
    html_3=urllib.request.urlopen(url_3)
    soup_8=BeautifulSoup(html_3,"html.parser")
    return soup_8




