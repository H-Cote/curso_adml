""" El siguiente algoritmo calcula la suma de los elementos impares de la  serie de fibonacci hasta el primer elemento superior a n. Por ejemplo, para n = 10, tenemos: f(10) = 1+1+3+5+13 = 23"""


def fibonacci_impares(n):
   # Obtenemos la lista con los valores de la serie de fibonacci 
    
    s0=[1,1] # Creamos una  lista con los valores iniciales de la serie. Eventualmente contendra n terminos de la serie. 
    impares=[] # Creamos un arreglo para colocar los valores impares que obtengamos
    impares_mayores=[] # Creamos un arreglo para colocar los impares que sean mayores al valor ingresado n. 
    
    for i in range (n): 
        
        suma=s0[i]+s0[i+1]  # Formula recursiva para obtener cada termino de la serie. 
        s0.append(suma)  # Colocamos los terminos obtenidos en el arreglo s0. 
        
   #Llenamos la lista 'impares'. Selecionamos aquellos terminos de la lista anterior s0 que sean impares. 
    for j in range (n):
        if (s0[j]%2)==0: # Si el termino de la lista es par. 
            a=0 # En si no hacemos nada, solo es para tener algo en if, pero lo que nos importa es else. 
        else:
            impares.append(s0[j]) # Si el termino es impar entonces lo agregamos al arreglo 'impares'
            
    #return impares
            
            
   # Obtenemos el termino siguente mayor a n

    for k in range (len(impares)): 
        
        if (impares[k]<=n): # si elemento en turno de la lista de impares es menor o igual a n.   
            tope=impares[k+1] # llamanos tope al el termino impar de la serie de fibonacci inmediato mayor a n.  
            impares_mayores.append(impares[k]) # Llenamos la lista 'ímpares_mayores' con los terminos de la lista 'impares' que cumplen impares[k]<=n.
    impares_mayores.append(tope) # agregamos el valor impar de la serie de fibonacci inmediato mayor a n.
    return sum(impares_mayores) # Realizamos la suma de los terminos. 

n=100000
#n=10 #debe dar 23   
print(fibonacci_impares(n))
