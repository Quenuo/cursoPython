"""Diseñar un algoritmo que nos diga el dinero que tenemos
(en euros y céntimos) después de pedirnos cuantas monedas tenemos
(de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)."""
numero_monedas_2euros=int(input("Introduce el numero de monedas de 2 euros: "))
numero_monedas_1euros=int(input("Introduce el numero de monedas de 1 euros: "))
numero_monedas_50centimos=int(input("Introduce el numero de monedas de 50 centimos: "))
numero_monedas_20centimos=int(input("Introduce el numero de monedas de 20 centimos: "))
numero_monedas_10centimos=int(input("Introduce el numero de monedas de 10 centimos: "))
centimos_totales=numero_monedas_10centimos*10+numero_monedas_20centimos*20+numero_monedas_50centimos*50
euros_totales=numero_monedas_1euros+numero_monedas_2euros*2
euros_totales+=centimos_totales//100
centimos_totales=centimos_totales%100 if centimos_totales>=100 else centimos_totales
#centimos_totales=centimos_totales%100 if centimos_totales>=100 else centimos_totales

print(f"Hay {euros_totales} euros y {centimos_totales} centimos")


