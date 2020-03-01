# https://omegaup.com/arena/OMIJALONLINE1/#problems/Numero-espirales

# n = input()
# n = int(n)

n = 2

def numeros_espirales(num):

    if(num == 1):
        return 1
    else:
        medio = False
        fin = False
        i = 0
        suma = 0
        while(not fin):
            if(i < num and not medio):
                i = i + 1
            elif(i >= num or medio):
                i = i - 1

            suma = suma + i

            if(i == num):
                medio = True
            elif(i == 1 and medio):
                fin = True

        return suma + numeros_espirales(num - 1)

    

print(numeros_espirales(n))