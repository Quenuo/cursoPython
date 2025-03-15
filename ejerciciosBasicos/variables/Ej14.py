#Dado un número de dos cifras,
# diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.
numero=input("Introduce un numero de dos cifras: ")
numero_invertido=numero[1]+numero[0]
print(f"El numero invertido de {numero} es {numero_invertido}")