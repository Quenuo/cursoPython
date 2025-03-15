"""La asociación de vinicultores tiene como política fijar un precio inicial
 al kilo de uva, la cual se clasifica en tipos A y B,
 y además en tamaños 1 y 2. Cuando se realiza la venta del producto,
 ésta es de un solo tipo y tamaño, se requiere determinar cuánto
 recibirá un productor por la uva que entrega en un embarque,
 considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos
cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
Realice un algoritmo para determinar la ganancia obtenida."""
precio_inicial = float(input("Introduce el precio inicial por kilos de la UVA (centimos):"))
tamanio = int(input("Introduce el tamanio:"))
tipo = input("Introduce el tipo de la UVA (A/B):")
kilos = int(input("Introduce cuantos kilos has vendido:"))

if tipo.upper() not in ("A", "B"):
    print("Escribe un tipo correcto")
elif precio_inicial<=0:
    print("Escribe un precio correcto")
elif tamanio not in (1,2):
    print("Introduce un tamaño correcto")
else:
    if tipo.upper()=="A":
        centimos=20 if tamanio==1 else 30
        precio_final=(precio_inicial+centimos/100)*kilos
        print(f"El precio final es {precio_final}")
    else:
        centimos=-30 if tamanio==1 else -50
        precio_final = (precio_inicial + centimos / 100) * kilos
        print(f"El precio final es {precio_final}")


