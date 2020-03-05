#! /usr/bin/python3
# This script will return a random pokemon
import requests, random, time

URL = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=964"

# time init

initialTime = time.time()

r = requests.get(url = URL)

data = r.json()

pokemonArray = []

for i in data['results']:
    pokemonArray.append(i['name'])

allPokemons = len(pokemonArray)

randomPokemon = pokemonArray[random.randint(0,allPokemons)]

finalTime = round(time.time() - initialTime, 2)

print(randomPokemon, "\nin "+str(finalTime)+" seconds")