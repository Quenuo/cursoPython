"""Dadas dos variables numéricas A y B, que el usuario debe teclear,
se pide realizar un algoritmo que intercambie los valores de ambas variables
y muestre cuanto valen al final las dos variables."""
a=int(input("Escribe el numero A: "))
b=int(input("Escribe el numero B: "))
print(f"Valores de A Y B antes de intercambiarse {a} {b}")
aux=a
a=b
b=aux
print(f"Valores de  a y b despues de intercambiarse {a} {b}")