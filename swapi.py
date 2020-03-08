#! /usr/bin/python3
# This script will return a random character of star wars
import requests
import random
import time
from concurrent import futures
from colorama import Fore, init

init()

initialTime = time.time()

def swapi(start, end):
    try:
        names = []
        url = "https://swapi.co/api/people/{}".format(start)
        if(end != None):
            limit = "https://swapi.co/api/people/?page={}".format(end)
        else:
            limit = None
        r = requests.get(url=url)
        data = r.json()
        while(url != limit):
            r = requests.get(url=url)
            data = r.json()
            for i in data['results']:
                names.append(i['name'])
            url = data['next']
    except requests.exceptions.RequestException as e:
        print(Fore.RED+" Star Wars Character not avaliable: request error", e)
    return names


ex = futures.ThreadPoolExecutor(max_workers=5)

wait_for = [
    ex.submit(swapi, '', '3'),
    ex.submit(swapi, '?page=3', '6'),
    ex.submit(swapi, '?page=6', None)
]

characters = []

for f in futures.as_completed(wait_for):
    characters += f.result()


finalTime = round(time.time() - initialTime, 2)
print(Fore.MAGENTA+"Random Star Wars Character: "+Fore.RED+characters[random.randint(0,len(characters))],Fore.GREEN+"(in "+str(finalTime)+" seconds)")

