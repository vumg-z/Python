# https://omegaup.com/arena/OOi2019Intermedios/#problems/pb-Triangulo

abc = input()

def triangle_validator(abc):

    abc = abc.split(" ")

    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])

    output = []
    output.append(c)
    output.append(b)
    output.append(a)

    if((a**2) + (b**2) == (c**2)):
        string = " "
        return string.join([str(elem) for elem in output])
    else:
        return "imposible"


print(triangle_validator(abc))
