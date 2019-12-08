# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

message = "¡Hola Mundo!"

print(message)

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

print("Introduce tu nombre")
nombre = input()
print("¡Hola "+nombre+"!")

# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas 
# distintas el nombre del usuario tantas veces como el número introducido.

# usaremos el nombre de arriba 

# print("Introduce tu nombre")

# nombre = input()

print("Escribe cuantas veces sera repetido")

repetir = int(input())

for i in range(0,repetir):
    print("¡Hola "+nombre+"!")

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por 
# pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que 
# tienen el nombre.

# usaremos el nombre de arriba
# print("Introduce tu nombre")
# nombre = input()

print("Tu nombre tiene: ", len(nombre) ," de letras")

# Escribir un programa que realice la siguiente operación aritmética (3+22⋅5)2.

print("Lo resultante de (3+2/2*5)**2 es: ", (((3+2)/(2*5))**2) )


# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene 
# en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
# calculado redondeado con dos decimales.

print("ingresa peso (kg)")
peso = float(input())

print("ingresa estatura (m)")
estatura = float(input())

imc = peso / estatura**2

print(imc)


# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

print("ingresa n")
n = int(input())

print("ingresa m")
m = int(input())

print("El cociente de ", n ,  " entre ", m,  " es: ", n // m , " el residuo de ", n ," /",  m  ,"es: ", n % m)


# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión.

inversion = float(input("ingresa la inversion"))
interes = float(input("ingresa el interes"))
anios = int(input("ingresa los años"))

print("El capital obtenido de la inversion es: " + str(round(inversion * (interes / 100 + 1 )**anios,2)))

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por
# pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseñaValidar = input("Ingresa una contraseña")

if contraseñaValidar == "contraseña":
    print("si")

input()