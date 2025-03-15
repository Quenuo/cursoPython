"""Escribe un programa que pida un nombre de usuario
y una contraseña y si se ha introducido “pepe”
 y “asdasd” se indica “Has entrado al sistema”, sino se da un error."""
nombre_usuario=input("Introduce el nombre de usuario: ")
contrasenia_usuario=input("Introduce tu contraseña: ")
if nombre_usuario=="pepe" and contrasenia_usuario=="asdasd":
    print("Has entrado en el sistema")
else:
    print("Error de autenticación el usuario o la contraseña son incorrectos")