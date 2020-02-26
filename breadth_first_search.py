# BFS
from collections import deque

graph = {}

graph["you"] = ["bob", "claire", "alice"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "jonny"]
graph["alice"] = ["peggy"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

# search method

def is_mango_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue: #mientras este vacia la cola
        person = search_queue.popleft()
        if(not person in searched):
            if is_mango_seller(person):
                print(person, "is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



search("you")