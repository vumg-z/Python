import random, time

random_numbers = []

def numbers(min, max):
    number = random.randint(min, max)
    if(number not in random_numbers):
        random_numbers.append(number)
    else:
        return numbers(min, max)    
