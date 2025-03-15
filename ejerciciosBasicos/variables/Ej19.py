"""Escribir un algoritmo para calcular la nota final de un estudiante,
considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1
y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante."""
numero_respuestas_correctas=int(input("Introduce el numero de respuestas correctas: "))
numero_respuestas_incorrectas=int(input("Introduce el numero de respuestas incorrectas: "))
numero_respuestas_blanco=int(input("Introduce el numero de respuestas en blanco: "))

numero_preguntas=numero_respuestas_blanco+numero_respuestas_incorrectas+numero_respuestas_correctas
puntuacion_aciertos=5*numero_respuestas_correctas
puntuacion_final=puntuacion_aciertos-numero_respuestas_incorrectas
puntuacion_perfecta=5*numero_preguntas
print(f"El estudiante ha sacado un {puntuacion_final}/{puntuacion_perfecta}")