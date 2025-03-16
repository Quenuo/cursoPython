"""Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos"."""
dado=int(input("Introduce el numero del dado: "))

if dado<=0 or dado>6:
    print("Escribe un numero de dado correcto")
elif dado==1:
    print("En la acara opuesta esta el 6")
elif dado==2:
    print("En la acara opuesta esta el 5")
elif dado==3:
    print("En la acara opuesta esta el 4")
elif dado==4:
    print("En la acara opuesta esta el 3")
elif dado==5:
    print("En la acara opuesta esta el 2")
elif dado==6:
    print("En la acara opuesta esta el 1")

