#Escribe un programa que lea un número e indique si es par o impar.

numero=int(input("Introduce un numero: "))

if numero%2==0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
