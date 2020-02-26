# Diccionarios

phone_book = {
    "uriel" : 3310249921,
    "jhon" : 3310231231
}

print("Un programa simple para añadir numeros de telefono")
print("[1] Añadir un contacto")
print("[2] Eliminar un contacto")
print("[3] Leer un contacto")
print("[4] Actualizar un contacto")

option = input()

if(option == "1"):
    print("añadir nombre")
    nombre = input()
    print("añadir numero")
    numero = input()
    phone_book[nombre] = numero
elif(option == "2"):
    print("escriba el nombre del contacto a eliminar")
    nombre = input()
    phone_book.pop(nombre)
elif(option == "3"):
    print("escriba el nombre del contacto a leer")
    nombre = input()
    if(nombre in  phone_book):
        print(phone_book[nombre])
    else:
        print("nombre no encontrado")
elif(option == "4"):
    print("Escriba el nombre del usuario a actualizar")
    nombre = input()
    if(nombre in phone_book):
        print("Ecriba el numero nuevo")
        numero = input()
        phone_book[nombre] = numero
    else:
        print("Usuario no encontrado")
    

print(phone_book)





