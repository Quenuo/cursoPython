#Calcular el perímetro y área de un rectángulo dada su base y su altura.
altura=int(input("Escribe la altura de un rectángulo "))
base=int(input("Escribe la base del rectangulo"))

area=altura*base
perimetro=2*(altura+base)

print(f"El area del rectángulo es {area} y su perimetro es {perimetro}")
