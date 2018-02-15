debug = True #Cambien este valor a False para pedir los datos al usuario

#Arreglo de entrenamiento
text = "6,3,9,5,1,7,1"

if not debug:
    text = input("Ingrese una secuencia de valores naturales separados por coma: ")

#Convertimos la cadena de caracteres en una lista
values = [int(i) for i in text.split(',')]

# Coloquen aquí su algoritmo de acomodo para acomodar la variable values

#------------------------------------------------

def sorting(lista): # definimos la funcion sorting, la cual requiere el ingreso de una lista de digitos
    lista_ordenada=[]  #Creamos un arreglo donde poner los valores de menor a mayor
    for j in range(len(lista)): #Ciclo para obtener el menor valor de cada nueva lista generada por el proceso de abajo. 
        el_menor=lista[0] # Tomamos el primer valor de la lista y lo considerarmos como el menor de la misma.  
        for i in range(len(lista)): #Ciclo para obtener el menor valor de una lista

            if (el_menor<=lista[i]): # Si el valor que tomamos es igual o menor a cada elemento de la lista
                el_menor=el_menor #entonces ese elemento, en efecto, es el menor de la lista. 
		
            else: #De lo contrario 
                el_menor=lista[i] # consideramos el otro elemento como el menor de la lista. 

        lista_ordenada.append(el_menor) #Agregamos el menor de la lista original a la lista ordenada. 
        lista.remove(el_menor) #Quitamos el menor de la lista original para asi tener una nueva lista. 
			      # A la cual, le aplicaremos el proceso anterior. 
    return (lista_ordenada) # El algoritmo anterior devuelve como resultado la lista ordenada. 


values1=sorting(values) # Aplicamos la funcion sorting que hicimos a la lista values. 
#------------------------------------------------

print(values1) # muestra el resultado la lista values ordenada en la terminal. 
