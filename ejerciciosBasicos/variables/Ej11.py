#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
import math

punto1=int(input("Primer numero: "))
punto2=int(input("Segundo numero: "))

#d=raizcuadradra(punto)
distancia=math.sqrt((punto2-punto1)**2)#al carecer de puntos y esto se resume a abs(punto2-punto1)
print(f"La distancia entre los puntos es {distancia}")
