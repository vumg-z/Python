array = [1,2,3,4,5]

def suma(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + suma(arr[1:])

print(suma(array))

