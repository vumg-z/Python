#! /usr/bin/python3
# This script will return a random pokemon
import requests, random, time
from colorama import Fore, init

init()

URL = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=964"

# time init

initialTime = time.time()

try:
    r = requests.get(url = URL)
    data = r.json()

    pokemonArray = []

    for i in data['results']:
        pokemonArray.append(i['name'])

    allPokemons = len(pokemonArray)

    randomPokemon = pokemonArray[random.randint(0,allPokemons)]

    finalTime = round(time.time() - initialTime, 2)

    print(Fore.MAGENTA+"Random Pokemon: "+Fore.BLUE+randomPokemon, Fore.GREEN+"(in "+str(finalTime)+" seconds)")

except requests.exceptions.RequestException as e:
    print("random pokemon not available:"+Fore.RED+" request error")
