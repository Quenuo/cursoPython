#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
from pyexpat import features

dia=int(input("Introduce el dia: "))
mes=int(input("Introduce el més: "))
anio=int(input("Introduce el año: "))
#Enero 1 febrero2 marzo3 abril4 mayo5 junio6 julio7 agosto8 septiembre9 octubre10 noviembr11 diciembre12

if dia>31 or dia<=0 or anio<=0 or mes<=0 or mes>12:
    print("Fecha incorrecta ")
else:
    if dia==31:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif mes==2:
        if dia<29:
            print("Fecha correcta")
        elif dia==29 and (anio%400==0 or (anio%4==0 and anio%100!=0)):
            print("Fecha correcta ")
        else:
            print("Fecha incorrecta")
    else:
        print("Fecha correcta ")





