 # Con esto consigo pasar un elemento del type objeto a type float. En este caso tenía un valor junto 
 #con el signo $ y tenía que quitar el signo $ para poder convertirlo a float y poder concatenarlo.
 #Aplica una funcion lambda que  dice que palabra tome en el valor [1:].
 #Es decir que en todo el valor menos en la primera posición  le aplique float. ej:$12.13 
 # Con esto consigo pasar un elemento del type objeto a tipo float.
 

(lambda palabra:float(palabra[1:])


#scraping Función que que muestra html de una web en jupiter
def show_html(html_str)
    print(bautifulsoup(str(html_str),"html.parser).prettify"())


# Scraping Recoger información de la página web
nombre_variable=requests.es("https...............................htn")

#Scraping creación de un objeto beautifulsoup para poder ver de forma ordenada y bonita el html y lo guardo en una variable

nombre_variable=beautifulsoup(pag.text,"html.parser")show_html(nombre_variable.tex)

#Scraping seleccionar el cuerpo o la parte del html en la que se encuentra la información que quiero obtener

nombre_variable2= nombre_variable.find(datos="el tag que define donde se encuentra la info y que tenemo que identificarlo en la web. ej <class=boodytext")show_html(str(nombre_variable2))

#Scraping buscar etiquetas con find_all (sirve para información que está etiquetada con una misma etiqueta, lo que hará será buscar en el cuerpo del html seleccionado
# todas las etiquetas iguales, ejempl que sean <a>)

#nombre_variable3=nombre_variable2.find_all("a")
show_html(nombre_variable3)

# Scraping  Recorro una lista con un for y extraemos la parte de la lista que nos interesa.

# for artist_name in nombre_variable3:
names=artis_names.contents
print(names)