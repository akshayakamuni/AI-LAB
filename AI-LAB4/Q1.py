graph = {
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
    "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Columbus", 144), ("Pittsburgh", 189)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
    "Pittsburgh": [("Cleveland", 189), ("Columbus", 185), ("Buffalo", 215), ("Philadelphia", 305)],
    "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150)],
    "Syracuse": [("Buffalo", 150), ("Boston", 312), ("New York", 254)],
    "Boston": [("Syracuse", 312), ("Providence", 50), ("Portland", 107)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "New York": [("Providence", 181), ("Syracuse", 254), ("Philadelphia", 97)],
    "Philadelphia": [("New York", 97), ("Baltimore", 101), ("Pittsburgh", 305)],
    "Baltimore": [("Philadelphia", 101)],
    "Portland": [("Boston", 107)]
}


def best_first_search(graph, start, goal):
    cost = 0
    priority_queue = [(start, cost, [start])]
    visited=[]
    while priority_queue:
        min = 0
        for i in range(len(priority_queue)):
            if priority_queue[0][1] > priority_queue[i][1]:
                min = i
        current_city, cost, path = priority_queue.pop(min)
        if current_city in visited:
            continue
        visited.append(current_city)
        if current_city == goal:
            return path, cost
        for neighbour, distance in graph[current_city]:
            if neighbour not in visited:
                new_cost = cost + distance
                new_path = path + [neighbour]
                priority_queue.append((neighbour, new_cost, new_path))



    return None, 0
path, total_cost = best_first_search(graph, "Syracuse", "Chicago")
print("Path:", "->".join(path))
print("Total cost:", total_cost)