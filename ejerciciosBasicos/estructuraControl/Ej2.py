#Algoritmo que pida un número y diga si es positivo, negativo o 0.
numero=float(input("Introduce un numero: "))

if numero>0:
    print(f"{numero} mayor que 0")
elif numero<0:
    print(f"{numero} menor que 0")
else:
    print("El numero es 0")


