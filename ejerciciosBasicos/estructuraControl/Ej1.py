#Algoritmo que pida dos números e indique si el primero es mayor
# que el segundo o no.
numero1=float(input("Introduce un numero: "))
numero2=float(input("Introduce un numero: "))

if numero2>numero1:
    print(f"El segundo {numero2} es mayor que el primero {numero1}")
elif numero1>numero2:
    print(f"El primero {numero1} es mayor que el segundo {numero2}")
else:
    print("Los números son iguales")



