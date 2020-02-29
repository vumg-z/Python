# https://omegaup.com/arena/OMIJALONLINE1/#problems/Supersticion

n = input()
n = int(n)
def supersticion(n):
    if(n % 2 is not 0):
        return("DEJARLO PASAR")
    else:
        return("SI")

print(supersticion(n))