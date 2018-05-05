#Importamos la funcion deque
from collections import deque
#Definimos la clase Grafo y asignamos valor vacio al diccionario de terminos
class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)
#Definimos la funcion agregar(Recibe un grafo y el elemento a agregar)
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})
#Definimos la funcion relacionar(Recibe un grafo, un origen y un destino)
def relacionar(grafo, origen, destino):
    #Relacionamos el origen con el destino
    grafo.relaciones[origen].append(destino) 
"""  
def profundidadPrimero(grafo, elementoInicial, elementoFinal, funcion, elementosRecorridos = []):
    if  elementoInicial==elementoFinal:
        print(elementoFinal)
        return
    if elementoInicial in elementosRecorridos:
        return
    funcion(elementoInicial)
    elementosRecorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, elementoFinal, funcion, elementosRecorridos)
"""
#Funcion De busqueda por Amplitud:
def anchoPrimero(grafo, elementoInicial, elementoFinal, funcion, cola = deque(), elementosRecorridos = []):
    #Recibimos el grafo en el que estamos trabajando, un origen, un destino, la instruccion para imprimir,
    #La funcion para hacer deque, Y una lista de elementos recorridos
    if elementoInicial==elementoFinal:
        print(elementoFinal)
        return
    #Retornamos El Destino cuando es encontrado.
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
    #Imprimimos cada elemento
        elementosRecorridos.append(elementoInicial)
    #Agregamos a la lista de Elementos Recorridos.
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])
    #Si el nodo tiene relaciones, las agregamos como lista, no como diccionario.
    if len(cola) != 0 :
        anchoPrimero(grafo, cola.popleft(), elementoFinal, funcion, cola, elementosRecorridos)
    #Mientras haya elementos en el Arreglo, seguiremos sacando elementos de forma FIFO   


####################################
#Funcion De busqueda por Profundidad:
def proPrimero(grafo, elementoInicial, elementoFinal, funcion, cola = deque(), elementosRecorridos = []):
    #Recibimos el grafo en el que estamos trabajando, un origen, un destino, la instruccion para imprimir,
    #La funcion para hacer deque, Y una lista de elementos recorridos
   if elementoInicial==elementoFinal:
       print(elementoFinal)
       return
    #Retornamos El Destino cuando es encontrado.
   if not elementoInicial in elementosRecorridos:
       funcion(elementoInicial)
    #Imprimimos cada elemento
       elementosRecorridos.append(elementoInicial)
    #Agregamos a la lista de Elementos Recorridos.
       if(len(grafo.relaciones[elementoInicial]) > 0):
           cola.extend(grafo.relaciones[elementoInicial])
    #Si el nodo tiene relaciones, las agregamos como lista, no como diccionario.
   if len(cola) != 0 :
       proPrimero(grafo, cola.pop(), elementoFinal, funcion, cola, elementosRecorridos)
    #Mientras haya elementos en el Arreglo, seguiremos sacando elementos de forma FILO   
 