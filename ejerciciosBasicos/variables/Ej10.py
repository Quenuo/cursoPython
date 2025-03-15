"""Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
"""
calificacion_parcial1=float(input("Introduce tu calificación parcial: "))
calificacion_parcial2=float(input("Introduce tu calificación parcial: "))
calificacion_parcial3=float(input("Introduce tu calificación parcial: "))
examen_final=float(input("Introduce tu calificación del examen final: "))
trabajo_final=float(input("Introduce tu calificación del trabajo final: "))

calificacion_parcial_promedio=0.55*(sum([calificacion_parcial1,calificacion_parcial2,calificacion_parcial3])/3)
examen_final*=0.3
trabajo_final*=0.15
calificacion_final=calificacion_parcial_promedio+examen_final+trabajo_final
print(f"Tu nota final es {calificacion_final}")
