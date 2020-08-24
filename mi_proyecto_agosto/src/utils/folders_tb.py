# Función genérica para abrir, crear, leer  y escribir archivos
import pandas as pd 
# Función para abrir el dataset. Esto pasa el archivo CSV (separado por comas) y transformo en un DataFrame

 def read_open(csv):    
    csv_df=pd.read_csv(name,index_col="date")
 x=read(csv=name)
 print(x)

    
# Función para leer url
    def read_url():
        url_def=urllib.request.urlopen(url)
x=read_url(url)
print(x)

# Función para leer url_3
    def read_url():
        url_def=urllib.request.urlopen(url)
x=read_url(url_3)
print(x)



# Función para abrir el dataset. Convertimos el csv en dataframe csv_df y establecemos que "date" es tipo fecha:
def open_csv(url):
    csv_df=pd.read_csv(url, parse_dates=["date"], index_col="date")
    return csv_df