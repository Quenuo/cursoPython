#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math

cateto1=int(input("Escribe un cateto del triangulo rectángulo: "))
cateto2=int(input("Escribe un cateto del triangulo rectángulo: "))

hipotenusa=math.sqrt(pow(cateto1,2)+pow(cateto2,2))
print(f"La hipotenusa del triangulo rectángulo es {hipotenusa}")
