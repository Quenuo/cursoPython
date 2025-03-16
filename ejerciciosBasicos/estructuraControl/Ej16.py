"""La política de cobro de una compañía telefónica es: cuando se realiza una llamada,
el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto,
50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo,
y si es otro día, en turno de mañana, 15 %, y en turno de tarde,
10 %. Realice un algoritmo para determinar
cuánto debe pagar por cada concepto una persona que realiza una llamada."""
minutos=int(input("Introduce el numero de minutos que durara la llamada"))
dia=input("Introduce el el dia")
if minutos<=0:
    print("Introuce los minutos correctos")
else:
    costo_minutos =0
    if minutos<=5:
        costo_minutos=minutos*1
    elif minutos <=8:
        costo_minutos=5+((minutos-5)*0.8)
    elif minutos <=10:
        costo_minutos=5+3*0.8+((minutos-8)*0.7)
    elif minutos>10:
        costo_minutos=5+3*0.8+2*0.7+((minutos-10)*0.5)
    print(f"Sin impuestos {costo_minutos}")
    if len(dia)<=0:
        print("Escribe un dia valido")
    elif dia.upper()=="DOMINGO":
        costo_final=costo_minutos*1.03
        print(f"Se debe de pagar {costo_final} por realizar la llamada")
    else:
        turno=input("Introduce el turno (TARDE/MAÑANA): ")
        if turno.upper() in ("TARDE","MAÑANA"):
            if turno.upper()=="TARDE":
                costo_final = costo_minutos * 1.1
                print(f"Se debe de pagar {costo_final} por realizar la llamada")
            elif turno.upper()=="MAÑANA":
                costo_final = costo_minutos * 1.15
                print(f"Se debe de pagar {costo_final} por realizar la llamada")
        else:
            print("Introduce un turno válido")
