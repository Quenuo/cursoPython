#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
grados_fahrenheit=float(input("Escribe los grados fahrenheit: "))
grados_celsius=(grados_fahrenheit-32)*5/9
#round se usa para redondear un numero a x decimales round(numero,numeroDecimalesMaximo))
print(f"{grados_fahrenheit}Fº son {round(grados_celsius,2)}Cº")