#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
# Calcula y muestra la distancia entre ellos.
import math

x1=int(input("Introduce el x1: "))
x2=int(input("Introduce el x2: "))
y1=int(input("Introduce el y1: "))
y2=int(input("Introduce el y2: "))

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"La distancia entre los puntos es {distancia:.2f}")
