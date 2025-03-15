#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
minutos=int(input("Introduce el numero de minutos: "))
horas=minutos//60
minutosFaltantes=minutos%60
print(f"{minutos} minutos son {horas} horas y {minutosFaltantes} minutos")