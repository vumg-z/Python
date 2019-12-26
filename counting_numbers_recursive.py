#  Write a recursive function to count the number of items in a list.

myList = ["item", "item","item"]

def counting(arr):
    if arr == []:
        return 0
    else:
        return 1 + counting(arr[1:])

print(counting(myList))