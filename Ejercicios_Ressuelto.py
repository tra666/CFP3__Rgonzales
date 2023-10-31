
# 1_Escribir un programa que almacene los meses del año (por ejemplo Enero, Feberero, Marzo......) en una lista y luego mostrar el resultado por pantalla.

# meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
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


#Este programa pide al usuario que introduzca su edad e ingresos mensuales. Luego, verifica si la edad es mayor o igual a 18 y si los ingresos son mayores 
# o iguales a $200.000. Si ambas condiciones son verdaderas, 
# el programa imprime que el usuario debe pagar el impuesto. Si no, imprime que el usuario no debe pagar el impuesto.


#5- Escribir un programa para una empresa de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes 
# por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar 
# gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.


# edad = int(input("Por favor, introduce la edad del cliente: "))

# if edad < 4:
#     print("El cliente puede entrar gratis.")
# elif 4 <= edad <= 18:
#     print("El precio de la entrada es $500.")
# else:
#     print("El precio de la entrada es $1000.")


#Este programa pide al usuario que introduzca la edad del cliente. Luego, verifica si el cliente es menor de 4 años
#entre 4 y 18 años, o mayor de 18 años. Dependiendo de la edad del cliente, el programa imprime el precio de la entrada correspondiente.


#6- Escribir un programa que solicite una contrasena y esta se deba volver a confirmar, el programa terminara cuando ambas contrasenas coincidan.

# contraseña = input("Por favor, introduce una contraseña: ")
# confirmacion = input("Por favor, confirma tu contraseña: ")

# while contraseña != confirmacion:
#     print("Las contraseñas no coinciden. Inténtalo de nuevo.")
#     contraseña = input("Por favor, introduce una contraseña: ")
#     confirmacion = input("Por favor, confirma tu contraseña: ")

# print("Las contraseñas coinciden. El programa ha terminado.")


#Este programa pide al usuario que introduzca una contraseña y luego la confirme. Si las contraseñas no coinciden
# el programa le pide al usuario que lo intente de nuevo. Esto continúa hasta que las contraseñas
#coinciden, momento en el cual el programa imprime un mensaje de confirmación y termina.




# def solicitar_contrasena():
#     while True:
#         contrasena = input("Por favor, ingrese su contraseña: ")
#         confirmacion = input("Por favor, confirme su contraseña: ")
#         if contrasena == confirmacion:
#             print("Las contraseñas coinciden. ¡Gracias!")
#             break
#         else:
#             print("Las contraseñas no coinciden. Inténtalo de nuevo.")

# solicitar_contrasena()



#Este programa solicita al usuario que ingrese una contraseña y luego la confirme. Si las contraseñas no coinciden, 
# el programa seguirá solicitando al usuario que ingrese y confirme la contraseña hasta que ambas coincidan. 
# Una vez que las contraseñas coinciden, el programa imprime un mensaje de agradecimiento y termina.

#True y break:

#El True en el bucle while se utiliza para crear un bucle infinito. Esto significa que el bucle continuará ejecutándose hasta que se encuentre una 
# instrucción break. El break se utiliza para salir del bucle. En este caso cuando las contraseñas ingresadas por el usuario coinciden, queremos salir del
# bucle. Por eso usamos break. Entonces, en resumen, el bucle while True: continuará solicitando al usuario que ingrese y confirme una contraseña 
# hasta que ambas contraseñas coincidan. En ese punto, se ejecuta la instrucción break, que termina el bucle. Después de eso
# el programa continúa con cualquier código que esté después del bucle (si lo hay), o termina si no hay más código.



# def solicitar_contrasena():
#     while True:

# Los dos puntos : en Python se utilizan para denotar el inicio de un bloque de código que está indentado. Este bloque de código puede ser el cuerpo
# de una función, el cuerpo de un bucle, una declaración condicional, etc. En tu código, def solicitar_contrasena(): 
# define una función llamada solicitar_contrasena. Los dos puntos : indican que el siguiente bloque de código indentado es el cuerpo de la función.
# Del mismo modo, en la línea while True:, los dos puntos : indican que el siguiente bloque de código indentado se debe ejecutar 
# mientras la condición después de while (en este caso, True) sea verdadera.


