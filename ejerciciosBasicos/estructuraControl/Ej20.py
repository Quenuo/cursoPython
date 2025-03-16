"""Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
 América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa
  en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

Zona	Ubicación	Costo/gramo
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
 esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso,
el rechazo de la entrega."""
zona=input("Escribe la ubicacion AmericaSur,AmericaNorte,Europa,AmericaCentral,Asia")
peso=int(input("Escribe el peso en gramos"))
if zona.upper() not in "AMERICASUR,AMERICANORTE,EUROPA,AMERICACENTRAL,ASIA":
    print("Escoge una zona correcta")
elif peso>5000:
    print("Paquete rechazado al superar los 5 kg")
else:
    if zona.upper()=="EUROPA":
        costo_gramos=10*peso
        print(f"Son {costo_gramos} euros por el equipaje")
    elif zona.upper()=="ASIA":
        costo_gramos=18*peso
        print(f"Son {costo_gramos} euros por el equipaje")
    elif zona.upper()=="AMERICACENTRAL":
        costo_gramos=20*peso
        print(f"Son {costo_gramos} euros por el equipaje")
    elif zona.upper()=="AMERICASUR":
        costo_gramos=21*peso
        print(f"Son {costo_gramos} euros por el equipaje")
    elif zona.upper()=="AMERICANORTE":
        costo_gramos=24*peso
        print(f"Son {costo_gramos} euros por el equipaje")