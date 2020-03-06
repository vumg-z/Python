# Simple program to get a random character from rick and morty

import requests, random, time
from colorama import Fore, init

init()
numbers = []
initalTime = time.time()

for i in range(0, 493):
    numbers.append(i)

numbers = str(numbers).replace(' ', '').replace('[', '').replace(']', '')

def getCharacters():
    try:
        names = []
        url = "https://rickandmortyapi.com/api/character/{}".format(numbers)
        r = requests.get(url=url)
        data = r.json()
        for i in data:
            names.append(i['name'])
        finalTime = str(round(time.time() - initalTime, 2))

        print(Fore.MAGENTA+"Rick and Morty random character: "+Fore.BLUE+names[random.randint(0, len(names))]+Fore.GREEN+" (in "+finalTime+" seconds)")

    except requests.exceptions.RequestException as e:
        print(Fore.RED+" Rick and Morty Character not avaliable: request error", e)

getCharacters()