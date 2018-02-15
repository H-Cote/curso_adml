"""
Este programa calcula el numero de 'turbopalindormos' entre 1 y un numero natural n. 

Definicion de 'turbopalindromo' (texto en latex): 

 Sea $x$ un numero de n digitos, $\left\lbrace x_0,x_1,x_2,...x_{n-1} \right\rbrace$, y sea $r$ una cantidad definida como:

\begin{equation}
	r=x + \sum_{i=0}^{n-1} (-1)^i * rot(x,x_i)
\end{equation}

donde $rot(x,\alpha)$ es la rotacion de los digitos de $x$ en $\alpha$ posiciones. Entonces $x$ sera un turbopalindromo si $r$ es un palindromo (puede ser un numero negativo). 

"""
#-------------------------------------------------------

"""Definimos las funciones a utilizar"""

# Convierte una lista de digitos en un valor entero positivo. Por ejemplo: [1,2,3] lo convierte en 123 
def conversor_lista_a_num( aList, base=10 ): # Los  argumentos son una lista y una base numerica, por default la base es decimal. 
    n = 0
    for d in aList:
        n = base*n + d
    return n

#-------------------------------------------------

# COnvierte un numero entero positivo en una lista de digitos. Por ejemplo: 123 lo convierte en [1,2,3]

def conversor_num_a_lista(valor):

    b = str(valor) # Convierte el numero en un string
    c = [] # Creamo el arreglo que contendra los digitos

    for digito in b:
        c.append (int(digito)) # Agregamos cada digito en el arreglo. 

    return (c)

#--------------------------------------------------


def rot(lista,a):

   # clon_lista=lista #Hacemos una copia de la lista para no modificar la original

    for i in range (a):

        ultimo_elemento=lista[len(lista)-1]#el -1 es porque la cuenta de los elementos inicia en cero.
        rota=[]#creamos un arreglo para colocarle el ultimo elemento
        rota.append(ultimo_elemento)#agregamos el elemento
        lista.pop(len(lista)-1)#Retiramos el ultimo elemento a la lista
        resultado=rota+lista #sumamos la lista que tiene al ultimo elemento a la lista que modificamos
       # print(resultado)
        lista=resultado# Ojo con el orden no es lo mismo que resultado=clon_lista
    return resultado


#----------------------------------------------------

#def palindromo(lista):

#    invertida=lista[::-1]
#    if lista==invertida:
#        print("r es un palindromo, por lo tanto x es un turbo palindromo")

    #else:
    #    print("pos no")
    
#-----------------------------------------------------

"""PROGRAMA"""

#-----------------------------------------------------

rango=int(input("Ingrese el rango: "))
#valor=int(input("ingrese un entero positivo x: "))






#numero_de_rotaciones=int(input("Ingrese el numero de rotaciones: "))
print("")

contador_de_turbo_palindromos=0

for valor in range (rango):

    valor=valor+1 # Le suamanos un 1 al valor porque por default el indice empieza en cero. 

    lista_del_valor = conversor_num_a_lista(valor) # A partir del valor creamos una lista con sus digitos  
    numero_de_rotaciones=len(lista_del_valor) # El numero de rotaciones es igual al numero de digitos del valor a rotar. 
	

    """Creamos un arreglo con los valores a sumar. Como dicta la expresion para r, el primer termino de la suma
    es el valor que ingresamos al inicio"""

    sumandos=[valor] #Arreglo con el valor ingresado


    """Con el siguiente ciclo rotamos el valor ingresado"""

    for i in range(numero_de_rotaciones):
        i=i+1 # Porque el indice i inicia en cero y rot(lis,0) no esta def.
        lista=conversor_num_a_lista(valor) # creamos una lista a partir del valor ingresado.
        lis_rot=rot(lista,i) #E sto es una lista con los valores de la lista anterior rotados i veces.
        num_rot=conversor_lista_a_num(lis_rot) # Convertimos la lista lis_rot a un numero
        num_rot_signo=pow(-1,i+2)*num_rot # De acuerdo con la expresion para r, multiplicamos cada termino
                                           #de la serie por +1 o -1 segun el indice i.

        sumandos.append(num_rot_signo) # El valor rotado con su signo asignado es agregado al arreglo
                                       # de los terminos a sumar.
    #    print(sumandos)

    #Sumamos los terminos
    suma_total=sum(sumandos)#Esta es r. Sumamos los terminos del arreglo anterior para obtener r.


#    print(suma_total)

    #Le cambiamos el signo a r, en caso de ser negativo, para que entre en la funcion de conversion a lista.
    if suma_total<0:
        r=suma_total*(-1)
    else:
        r=suma_total

    # Ahora r es un posible turbopalindromo.
    posible_tp=conversor_num_a_lista(r) #Esta es una lista con los digitos del posible turbopalindromo.

# Eliminamos la funcion palindromo(), y en su lugar se coloco como parte del PROGRAMA:

    invertida=posible_tp[::-1]
    if posible_tp==invertida:
            contador_de_turbo_palindromos=contador_de_turbo_palindromos+1
            #print("r es un palindromo, por lo tanto x es un turbo palindromo")
print("Hay", contador_de_turbo_palindromos , "turbopalindromos en el rango")
print("")
