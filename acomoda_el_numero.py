# https://omegaup.com/arena/AAGS/#problems/AcomodandoOMI

# n = input() # 5
array = input()  # 14 2 1 17 23

def binarySearch(arr, number):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        guess = arr[mid]

        if guess == number:
            return mid
        elif guess < number:
            start = mid
        else:
            end = mid


def acomoda_el_numero(array):

    position = array[0]
    array.sort()
    # look in what index is position
    return binarySearch(array, position)


array = array.split(" ")
for i, val in enumerate(array):
    array[i] = int(val)
        
print(acomoda_el_numero(array))
