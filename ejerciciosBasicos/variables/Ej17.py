"""Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
 El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
 Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
HH = int(input("Introduce la hora de salida (HH): "))
MM = int(input("Introduce los minutos de salida (MM): "))
SS = int(input("Introduce los segundos de salida (SS): "))
segundos_t=int(input("Introduce los segundos tardados"))
segundos_totales=HH * 3600 + MM * 60 + SS + segundos_t

# Extraemos la hora, minutos y segundos tras el viaje
hora_llegada = (segundos_totales // 3600) % 24
minuto_llegada = (segundos_totales % 3600) // 60
segundo_llegada = segundos_totales % 60

print(f"La hora de llegada será {hora_llegada:02}:{minuto_llegada:02}:{segundo_llegada:02}")

