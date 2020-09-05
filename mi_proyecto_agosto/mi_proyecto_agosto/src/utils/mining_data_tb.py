# Modulo relacionado con la disputa y limpieza  de datos
import pandas as pd
import re
import sys



#Quitar los puntos separadores  de un número en formato str
def quitar_puntos(text):
    text= re.sub('[.]', '',text) 
    return text


#Seleccionar una parte de una cadena

def seleccion_str(text,col1,col2):
    resultado=text[col1:col2]
    return resultado
    
# seleccionar en una cadena precios vacunas

def seleccion_str2(text,col1):
    resultado=text[col1]
    return resultado

#quitar tags

from bs4 import BeautifulSoup, NavigableString, Tag

def tags(element):
    for p in element:
        if isinstance(p,NavigableString):
            continue
        if isinstance(p,Tag):
            print(p)
