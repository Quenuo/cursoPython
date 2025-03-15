"""Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter
‘sexo’ y muestre el
mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad
es mayor o igual a
dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo,
pero el sexo sea ‘M’, debe
imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones
se debe mostrar ‘NO ACEPTADA’."""
#PSOIZADO
nota=float(input("Introduce tu nota"))
edad=int(input("Introduce tu edad"))
genero=input("Introduce tu generero M/F")
if nota>=5 and edad>=18:
    if genero=="F":
        print("Las leyes de cuotas estas justificadas, ACEPTADA")
    elif genero=="M":
        print("Eres el genero opresor , POSIBLE, VIVA PSOE ; PP Y PODEMOS")
    else:
        print("Muy y mucho feministas pero solo hay dos géneros, lo siento por el que se sienta megalodón")
else:
    print("PSOEIZADO, confiaste en el PSOE y acabaste psoizado, NO ACEPTADA")