"""El director de una escuela está organizando un viaje de estudios,
y requiere determinar cuánto debe cobrar a cada alumno
y cuánto debe pagar a la compañía de viajes por el servicio.
La forma de cobrar es la siguiente: si son 100 alumnos o más,
el costo por cada alumno es de 65 euros; de 50 a 99 alumnos,
el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros,
sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a
la compañía de autobuses y lo que debe pagar cada alumno por el viaje."""
numero_alumnos=int(input("Introduce el numero de alumnos: "))
if numero_alumnos<=0:
    print("No puede haber menos de 0 alumnos")
elif numero_alumnos<30:
    costo_alumno=4000/numero_alumnos
    print(f"El coste de renta del autobús  es de 4000 euros y cada alumno debe de pagar {costo_alumno:.2f}")

elif 30 <= numero_alumnos < 50:#es simplificado de alumnos>=30 and alumnos <50
    costo_alumno=95*numero_alumnos
    print(f"El costo del autobus por {numero_alumnos} alumnos es de {costo_alumno} euros y cada alumno dene de pagar 95")
elif 50<= numero_alumnos <100:
    costo_alumno = 70 * numero_alumnos
    print(f"El costo del autobus por {numero_alumnos} alumnos es de {costo_alumno} euros y cada alunno debe de pagar 70")
else:
    costo_alumno = 65 * numero_alumnos
    print(f"El costo del autobus por {numero_alumnos} alumnos es de {costo_alumno} euros y cada alumno debe de pagar 65")

