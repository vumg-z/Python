# https://omegaup.com/arena/OOi2019Intermedios/#problems/pb-Suma-TRiple
n = input()
cases = int(n)

def triple_sum(n):
    numbers = [1, 1, 2]
    if(n > 3):
        for i in range(3, n):
            triple_suma = (numbers[i - 1] + numbers[i - 2] + numbers[i - 3])
            numbers.append(triple_suma)
        return numbers
    else:
        limit = len(numbers) - n 
        for i in range(0, limit):
            numbers.pop()
    return numbers


array = triple_sum(cases)

output = " "
output = output.join([str(elem) for elem in array])

print(output)