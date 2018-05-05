#Importamos las funciones de nuestro programa graph.py.
from graph import *
#Importamos la libreria colorama para dar color al texto.
from colorama import *
#Asignamos valores a nuestras variables Nodos.
e1="E1"
e2="E2"
e3="E3"
a="A"
b="B"
c="C"
d="D"
e="E"
f="F"
g="G"
h="H"
i="I"
j="J"
k="K"
l="L"
m="M"
n="N"
o="O"
p="P"
q="Q"
r="R"
canchas="CANCHAS"
pingpong="MESAS"
#Igualamos la variavle grafo a la funcion grafo en graph.py.
grafo = Grafo()
#La funcion Agregar de graph.py recibe un grafo y un elemento de ese grafo.
agregar(grafo, e1)
agregar(grafo, e2)
agregar(grafo, e3)
agregar(grafo, a)
agregar(grafo, b)
agregar(grafo, c)
agregar(grafo, d)
agregar(grafo, e)
agregar(grafo, f)
agregar(grafo, g)
agregar(grafo, h)
agregar(grafo, i)
agregar(grafo, j)
agregar(grafo, k)
agregar(grafo, l)
agregar(grafo, m)
agregar(grafo, n)
agregar(grafo, o)
agregar(grafo, p)
agregar(grafo, q)
agregar(grafo, r)
agregar(grafo, canchas)
agregar(grafo, pingpong)
#La funcion relacionar de graph.py recive un grafo, un origen y un destino.
relacionar(grafo, e1,j)
relacionar(grafo, e2, f)
relacionar(grafo, e2, j)
relacionar(grafo, e2, canchas)
relacionar(grafo, e3, a)
relacionar(grafo, e3, pingpong)
relacionar(grafo, a, e3)
relacionar(grafo, a, b)
relacionar(grafo, a, p)
relacionar(grafo, a, r)
relacionar(grafo, b, a)
relacionar(grafo, b,c)
relacionar(grafo, b, d)
relacionar(grafo, b, f)
relacionar(grafo, b, r)
relacionar(grafo, c, b)
relacionar(grafo, c, f)
relacionar(grafo, c, canchas)
relacionar(grafo, d, b)
relacionar(grafo, d, l)
relacionar(grafo, d, o)
relacionar(grafo, e, g)
relacionar(grafo, e, h)
relacionar(grafo, e, i)
relacionar(grafo, e, k)
relacionar(grafo, f, e2)
relacionar(grafo, f, b)
relacionar(grafo, f, c)
relacionar(grafo, f, g)
relacionar(grafo, f, j)
relacionar(grafo, g, e)
relacionar(grafo, g, f)
relacionar(grafo, g, h)
relacionar(grafo, g, j)
relacionar(grafo, h, e)
relacionar(grafo, h, g)
relacionar(grafo, h, i)
relacionar(grafo, h, j)
relacionar(grafo, i, e)
relacionar(grafo, i, h)
relacionar(grafo, j, e1)
relacionar(grafo, j, e2)
relacionar(grafo, j, f)
relacionar(grafo, j, g)
relacionar(grafo, j, h)
relacionar(grafo, k, e)
relacionar(grafo, k, l)
relacionar(grafo, l, d)
relacionar(grafo, l, k)
relacionar(grafo, l, o)
relacionar(grafo, o, d)
relacionar(grafo, o, l)
relacionar(grafo, o, p)
relacionar(grafo, p, a)
relacionar(grafo, p, o)
relacionar(grafo, r, a)
relacionar(grafo, r, b)
relacionar(grafo, r, canchas)
relacionar(grafo, r, pingpong)
relacionar(grafo, canchas, e2)
relacionar(grafo, canchas, c)
relacionar(grafo, canchas, r)
relacionar(grafo, pingpong, e3)
relacionar(grafo, pingpong, r)
relacionar(grafo, e1, e1)
relacionar(grafo, e2, e2)
relacionar(grafo, e3, e3)
relacionar(grafo, a, a)
relacionar(grafo, b, b)
relacionar(grafo, c, c)
relacionar(grafo, d, d)
relacionar(grafo, e, e)
relacionar(grafo, f, f)
relacionar(grafo, g, g)
relacionar(grafo, h, h)
relacionar(grafo, i, i)
relacionar(grafo, j, j)
relacionar(grafo, k, k)
relacionar(grafo, l, l)
relacionar(grafo, m, m)
relacionar(grafo, n, n)
relacionar(grafo, o, o)
relacionar(grafo, p, p)
relacionar(grafo, q, q)
relacionar(grafo, r, r)
relacionar(grafo, canchas, canchas)
relacionar(grafo, pingpong, pingpong)
#Definimos la funcion Imprimir, por que la funciones 
#profundidadPrimero y anchoPrimero, la requieren como parametro
def imprimir (elemento):
    print (elemento,"-->") 
#Imprimimos las relaciones del grafo
print("\nRelaciones!\n")
print(grafo.relaciones,"\n")
#Llamamos la funcion profundidadPrimero de graph.py
#Enviando como parametros:
#1 Un grafo
#2 El nodo Inicial
#3 El nodo Destino
#4 La funcion Imprimir
"""
print (Fore.BLACK+Back.WHITE+"Profundidad\n")
auxDestinoP = input("Ingresa tu Destino: ")
destinoP = auxDestinoP.upper()
profundidadPrimero(grafo, e2, destinoP, imprimir)
#Llamamos la funcion anchoPrimero de graph.py
#Enviando como parametros:
#1 Un grafo
#2 El nodo Inicial
#3 El nodo Destino
#4 La funcion Imprimir
"""
print (Fore.BLACK+Back.WHITE+"\nAmplitud\n")
auxDestinoA = input("Ingresa tu Destino: ")
destinoA = auxDestinoA.upper()
anchoPrimero(grafo, e2, destinoA, imprimir)



print (Fore.BLACK+Back.CYAN+"\nProfundidad\n")
auxDestinoA = input("Ingresa tu Destino: ")
destinoA = auxDestinoA.upper()
proPrimero(grafo, e2, destinoA, imprimir)