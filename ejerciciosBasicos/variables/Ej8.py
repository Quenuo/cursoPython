#Un vendedor recibe un sueldo base mas un 10% extra por comisión
# de sus ventas, el vendedor desea saber cuanto dinero obtendrá
# por concepto de comisiones por las tres ventas que realiza en el mes y
# el total que recibirá en el mes tomando en cuenta su sueldo base
# y comisiones.
sueldo_base=int(input("Introduce el sueldo base del vendedor: "))
venta1=int(input("Introduce la venta 1 "))
venta2=int(input("Introduce la venta 2 "))
venta3=int(input("Introduce la venta 1 "))


comision_total=0.1*(venta1+venta3+venta2)
sueldo_total=sueldo_base+comision_total
print(f"Recibira {comision_total} por las comisiones de las tres ventas y {sueldo_total} del total")



