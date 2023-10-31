
# 1_Escribir un programa que almacene los meses del año (por ejemplo Enero, Feberero, Marzo......) en una lista y luego mostrar el resultado por pantalla.

#meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# for mes in meses:
#     print(mes)



# Lista de los meses del año
# meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
#          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# # Mostrar los meses
# print('\n'.join(meses))


# 2- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# palabra = input("Por favor, ingresa una palabra: ")
# for i in range(10):
#     print(palabra)


# 3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# numero = int(input("Introduce un número entero: "))
# if numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

# pide al usuario que introduzca un número entero. Luego, utiliza el operador de módulo (%) para calcular el resto de la división del número por 2.
# Si el resto es 0, significa que el número es par. Si no, el número es impar. Finalmente, imprime el resultado.


# 4- Para pagar un determinado impuesto se debe ser mayor de 18 años y tener un ingreso mensual igual o mayor a $200.000. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario debe pagar el impuesto o no.

# edad = int(input("Por favor, introduce tu edad: "))
# ingresos = float(input("Por favor, introduce tus ingresos mensuales: "))

# if edad >= 18 and ingresos >= 200000:
#     print("Debes pagar el impuesto.")
# else:
#     print("No debes pagar el impuesto.")


#pide al usuario que introduzca su edad e ingresos mensuales. Luego, verifica si la edad es mayor o igual a 18 y si los ingresos son mayores o iguales a $200.000.
#Si ambas condiciones son verdaderas, el programa imprime que el usuario debe pagar el impuesto. Si no, imprime que el usuario no debe pagar el impuesto.


#5- Escribir un programa para una empresa de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes 
# por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar 
# gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.


edad = int(input("Por favor, introduce la edad del cliente: "))

if edad < 4:
    print("El cliente puede entrar gratis.")
elif 4 <= edad <= 18:
    print("El precio de la entrada es $500.")
else:
    print("El precio de la entrada es $1000.")


#pide al usuario que introduzca la edad del cliente. Luego, verifica si el cliente es menor de 4 años
#entre 4 y 18 años, o mayor de 18 años. Dependiendo de la edad del cliente, el programa imprime el precio de la entrada correspondiente.


#6- Escribir un programa que solicite una contrasena y esta se deba volver a confirmar, el programa terminara cuando ambas contrasenas coincidan.

contrasena = input("Por favor, introduce una contraseña: ")
confirmacion = input("Por favor, confirma tu contraseña: ")

while contrasena != confirmacion:
    print("Las contraseñas no coinciden. Inténtalo de nuevo.")
    contrasena = input("Por favor, introduce una contraseña: ")
    confirmacion = input("Por favor, confirma tu contraseña: ")

print("Las contraseñas coinciden. El programa ha terminado.")

#pide al usuario que introduzca una contraseña y luego la confirme. Si las contraseñas no coinciden
# el programa le pide al usuario que lo intente de nuevo. Esto continúa hasta que las contraseñas
#coinciden, momento en el cual el programa imprime un mensaje de confirmación y termina.

















