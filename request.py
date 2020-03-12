import requests, random, time
from colorama import Fore, init

init()

URL = "http://127.0.0.1:5000/hello"

# time init

initialTime = time.time()

try:
    r = requests.get(url = URL)
    data = r.json()

    finalTime = round(time.time() - initialTime, 2)

    print(data)


except requests.exceptions.RequestException as e:
    print(Fore.RED+" request error")
