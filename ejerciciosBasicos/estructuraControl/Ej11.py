"""Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triangulo es,
teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno."""
import math

primer_lado=float(input("Introduce el cateto "))
segundo_lado=float(input("Introduce el cateto "))
tercer_lado=float(input("Introduce el cateto "))

hipotenusa=math.sqrt(primer_lado**2+segundo_lado**2)
#ladoA ** 2 + ladoB ** 2 == ladoC ** 2 or ladoB ** 2 + ladoC ** 2 == ladoA ** 2 or ladoC ** 2 + ladoA ** 2 == ladoB ** 2:
if hipotenusa==tercer_lado:
    print("Es un triangulo rectángulo")
else:
    if tercer_lado==segundo_lado and tercer_lado==primer_lado:
        print("Es un triangulo equilátero")
    elif segundo_lado==tercer_lado or segundo_lado==primer_lado:
        print("Es un triangulo isósceles")
    else:
        print("Es un triangulo escaleno")