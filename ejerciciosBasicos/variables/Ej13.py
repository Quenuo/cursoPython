"""Realizar un algoritmos que lea un número y que muestre su raíz cuadrada
y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular
la raíz cúbica, ¿Cómo se puede calcular?"""
import math

numero=int(input("Introduce un numero: "))
raiz_cuadrada=math.sqrt(numero)
raiz_cubica=numero**(1/3)
print(f"La raiz cuadrada y cubica de {numero} es {raiz_cuadrada:.2f} y {raiz_cubica:.2f}")
