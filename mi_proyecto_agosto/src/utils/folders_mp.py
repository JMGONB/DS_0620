# Función genérica para abrir, crear, leer  y escribir archivos
    pandas  pd 
# Función para abrir el dataset. Esto pasa el archivo CSV (separado por comas) y transformo en un DataFrame

 def read(csv):    
    csv_df=pd.read_csv(name,index_col= )
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