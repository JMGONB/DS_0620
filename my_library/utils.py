 # Con esto consigo pasar un elemento del type objeto a type float. En este caso tenía un valor junto 
 #con el signo $ y tenía que quitar el signo $ para poder convertirlo a float y poder concatenarlo.
 #Aplica una funcion lambda que  dice que palabra tome en el valor [1:].
 #Es decir que en todo el valor menos en la primera posición  le aplique float. ej:$12.13 
 # Con esto consigo pasar un elemento del type objeto a tipo float. 
(lambda palabra:float(palabra[1:])
