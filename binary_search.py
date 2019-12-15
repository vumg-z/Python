# Binary Search

def binarySearch(arr,number):
    low = 0;
    high = len(arr) - 1;
    steps = 0;
    while low <= high:
        mid = (low + high) // 2;
        guess = arr[mid];
        if number == guess:
            return mid;
        elif number > guess:
            low = mid + 1;
        else:
            high = mid - 1;
        

my_list = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(my_list,10))
