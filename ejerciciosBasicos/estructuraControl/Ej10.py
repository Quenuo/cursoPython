"""Algoritmo que pida los puntos centrales x1,y1,x2,y2
y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas"""
import math

# Solicitar las coordenadas de los centros y los radios de las circunferencias
x1 = float(input("Introduce la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Introduce la coordenada y del centro de la primera circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))

x2 = float(input("Introduce la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Introduce la coordenada y del centro de la segunda circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))

# Calcular la distancia entre los centros
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Clasificación de las circunferencias
if d == 0 and r1 == r2:
    print("Las circunferencias son concéntricas.")
elif d > r1 + r2:
    print("Las circunferencias son exteriores.")
elif d == r1 + r2:
    print("Las circunferencias son tangentes exteriores.")
elif r1 - r2 < d < r1 + r2:
    print("Las circunferencias son secantes.")
elif d == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")
elif d < abs(r1 - r2):
    print("Las circunferencias son interiores.")
