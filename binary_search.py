#Binary search

def binarySearch(arr,number):
    start = 0;
    end = len(arr) - 1;
    
    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]
        
        if guess == number:
            return mid
        elif guess < number:
            start = mid + 1
        else:
            end = mid - 1
        

my_list = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(my_list,10))
