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

def fitness(path):
    return 1/cost(path)


def initial_population(size):
    pop = []
    for _ in range(size):
        p = list(range(8))
        random.shuffle(p)
        pop.append(p)
    return pop


def selection(pop):
    pop.sort(key=cost)
    return pop[:len(pop)//2]


def single_point(parent1,parent2):

    point = random.randint(1,len(parent1)-2)

    child = parent1[:point]

    for gene in parent2:
        if gene not in child:
            child.append(gene)

    return child


def two_point(parent1,parent2):

    p1 = random.randint(0,len(parent1)-3)
    p2 = random.randint(p1+1,len(parent1)-1)

    child = [-1]*len(parent1)

    child[p1:p2] = parent1[p1:p2]

    ptr = 0
    for gene in parent2:
        if gene not in child:
            while child[ptr] != -1:
                ptr += 1
            child[ptr] = gene

    return child


def mutate(path):

    i,j = random.sample(range(len(path)),2)
    path[i],path[j] = path[j],path[i]
    return path


def genetic_algorithm(pop_size=20,generations=200,crossover="single"):

    pop = initial_population(pop_size)

    for _ in range(generations):

        pop = selection(pop)

        children = []

        while len(children) < pop_size:

            p1,p2 = random.sample(pop,2)

            if crossover == "single":
                child = single_point(p1,p2)
            else:
                child = two_point(p1,p2)

            if random.random() < 0.1:
                child = mutate(child)

            children.append(child)

        pop = children

    best = min(pop,key=cost)

    return best,cost(best)


print("\nGenetic Algorithm Results\n")

path,c = genetic_algorithm(crossover="single")
print("Single Point Crossover")
print("Path =",[cities[i] for i in path])
print("Cost =",c)

print()

path,c = genetic_algorithm(crossover="two")
print("Two Point Crossover")
print("Path =",[cities[i] for i in path])
print("Cost =",c)