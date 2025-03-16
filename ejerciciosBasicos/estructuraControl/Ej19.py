"""Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente."""
mes=int(input("Escribe el día del més "))
if mes<1 or mes>12:
    print("Mes invalido")
    print("31 dias")
elif mes==2:
    print("28 dias o 29 dias si es bisiesto")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        print("31 días")
    else:
        print("30 días")