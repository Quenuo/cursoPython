"""Algoritmo que pida tres números y los muestre ordenados
(de mayor a menor);
"""
numero1=float(input("Introduce un numero: "))
numero2=float(input("Introduce un numero: "))
numero3=float(input("Introduce un numero: "))
# Ordenar los números con if-else
if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(f"Los números ordenados de mayor a menor son: {numero1}, {numero2}, {numero3}")
    else:
        print(f"Los números ordenados de mayor a menor son: {numero1}, {numero3}, {numero2}")
elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        print(f"Los números ordenados de mayor a menor son: {numero2}, {numero1}, {numero3}")
    else:
        print(f"Los números ordenados de mayor a menor son: {numero2}, {numero3}, {numero1}")
else:
    if numero1 >= numero2:
        print(f"Los números ordenados de mayor a menor son: {numero3}, {numero1}, {numero2}")
    else:
        print(f"Los números ordenados de mayor a menor son: {numero3}, {numero2}, {numero1}")

