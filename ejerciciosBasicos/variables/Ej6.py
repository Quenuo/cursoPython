#Calcular la media de tres números pedidos por teclado.

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero: "))
numero3=int(input("Introduce un numero: "))
arrayNumeros=[numero1,numero2,numero2]
media=sum(arrayNumeros)/len(arrayNumeros)
print(f"La media de los numeros es {media}")
