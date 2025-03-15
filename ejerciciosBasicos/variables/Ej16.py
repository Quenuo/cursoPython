"""Dos vehículos viajan a diferentes velocidades (v1 y v2)
y están distanciados por una distancia d. El que está detrás viaja
a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia
entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido
al otro."""
v1=float(input("Introduce la velocidad del vehiculo 1: "))
v2=float(input("Introduce la velocidad del vehiculo 2: "))
d=int(input("Introduce la distancia"))
#v=d/t t=d/(v1-v2)
tiempo=d/(v1-v2) #en metros segundos
print(f"Lo alcanzara en {tiempo*60:.2f} minutos")
