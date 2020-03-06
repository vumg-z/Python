#! /usr/bin/python3
# This script will return a random character of star wars
import requests, random, time
from colorama import Fore, init

init()

# time init

initialTime = time.time()

names = []

try:
    url = "https://swapi.co/api/people/"    
    r = requests.get(url = url)
    data = r.json()
    while(data['next'] is not None):
        r = requests.get(url = url)
        data = r.json()
        for i in data['results']:
            names.append(i['name'])
        url =  data['next']
except requests.exceptions.RequestException as e:
    print(Fore.RED+" Star Wars Character not avaliable: request error")

finalTime = round(time.time() - initialTime, 2)

print(Fore.BLUE+names[random.randint(0,len(names))] + Fore.GREEN+" (in "+str(finalTime)+" seconds)")