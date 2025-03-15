#Crea un programa que pida al usuario dos números
# y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.
numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero: "))
if numero2!=0:
    print(f"{numero1/numero2:.2f}")
else:
    print(f"{numero2} es cero y no se puede dividir entre cero")