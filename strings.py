# Strings

string = "Hola mundo"


print("Hola" in string) # true

# upper

stringUp = string.upper()

# lower

stringLow = string.lower()

# isupper

print(stringLow)

# Pequeño programa medio emo

print("Como estas?")
sentimiento = input()

if sentimiento.lower() == "bien":
    print("yo tambien me siento bien")
else:
    print("ten un buen dia")
    
# isalnum program example, isalnum valida que solamente sean numeros y letras las que se puedan introducir


while True:
    print("Select a new password (letters and numbers only)")
    password = input()
    
    if password.isalnum():
        break
    
    print("Invalid format password")
    
# Join()
# Split()

mensaje = "hola mi nombre es uriel"
testo = " "

print(testo.join(['cats','rats','bats']))

print(mensaje.split())

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# removing white space

# strip()

mensaje = "  hola mundo  "
print(mensaje.strip(' ')) # elimina espacios al rededor

import pyperclip
pyperclip.copy("Esto es piperclip")
pyperclip.paste()


    
    
    
