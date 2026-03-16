import random

cities = ['A','B','C','D','E','F','G','H']

graph = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]


def cost(path):
    total = 0
    for i in range(len(path)-1):
        total += graph[path[i]][path[i+1]]
    total += graph[path[-1]][path[0]]
    return total


def random_path(n):
    p = list(range(n))
    random.shuffle(p)
    return p


def neighbors(path):
    neigh = []
    for i in range(len(path)):
        for j in range(i+1,len(path)):
            newp = path.copy()
            newp[i],newp[j] = newp[j],newp[i]
            neigh.append(newp)
    return neigh


def local_beam_search(k,iterations=100):

    states = [random_path(8) for _ in range(k)]

    for _ in range(iterations):

        all_neighbors = []

        for s in states:
            all_neighbors.extend(neighbors(s))

        all_neighbors.sort(key=cost)

        states = all_neighbors[:k]

    best = min(states,key=cost)
    return best,cost(best)


print("Local Beam Search Results\n")

for k in [3,5,10]:

    path,c = local_beam_search(k)

    print("Beam Width =",k)
    print("Best Path =",[cities[i] for i in path])
    print("Cost =",c)
    print()