adj = {
    "Portland": [("Boston", 107)],
    "Boston": [("Syracuse", 312), ("New York", 215), ("Providence", 50)],
    "Providence": [("Boston", 50), ("New York", 181)],
    "New York": [("Syracuse", 254), ("Boston", 215), ("Philadelphia", 97), ("Providence", 181)],
    "Syracuse": [("Buffalo", 150), ("Philadelphia", 253), ("Boston", 312), ("New York", 254)],
    "Philadelphia": [("Pittsburgh", 305), ("Baltimore", 101), ("New York", 97), ("Syracuse", 253)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Buffalo": [("Syracuse", 150), ("Detroit", 256), ("Cleveland", 189), ("Pittsburgh", 215)],
    "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Philadelphia", 305), ("Baltimore", 247), ("Buffalo", 215)],
    "Detroit": [("Buffalo", 256), ("Cleveland", 169), ("Chicago", 283)],
    "Cleveland": [("Buffalo", 189), ("Detroit", 169), ("Chicago", 345), ("Columbus", 144), ("Pittsburgh", 134)],
    "Columbus": [("Cleveland", 144), ("Pittsburgh", 185), ("Indianapolis", 176)],
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "Indianapolis": [("Columbus", 176), ("Chicago", 182)],
}

class Node:
    def __init__(self, city, parent, cost):
        self.city = city
        self.parent = parent
        self.cost = cost  

def get_path(node):
    path = []
    while node:
        path.append(node.city)
        node = node.parent
    path.reverse()
    return path

def pop_min(frontier):
    min_i = 0
    for i in range(1, len(frontier)):
        if frontier[i].cost < frontier[min_i].cost:
            min_i = i
    return frontier.pop(min_i)

def best_first_search(start, goal):
    frontier = []         
    explored = set()   
    best_cost = {}   # best cost found for each city

    frontier.append(Node(start, None, 0))
    best_cost[start] = 0
    explored_count = 0

    while len(frontier) > 0:
        curr = pop_min(frontier)  
        explored_count += 1

        if curr.city == goal:
            return curr, explored_count

        if curr.city in explored:
            continue
        explored.add(curr.city)

        for (next_city, w) in adj.get(curr.city, []):
            new_cost = curr.cost + w

            # push only if we found a better cost
            if next_city not in explored and (next_city not in best_cost or new_cost < best_cost[next_city]):
                best_cost[next_city] = new_cost
                frontier.append(Node(next_city, curr, new_cost))

    return None, explored_count

if __name__ == "__main__":
    start_city = "Syracuse"
    goal_city = "Chicago"
    ans, count = best_first_search(start_city, goal_city)

    if ans:
        path = get_path(ans)
        print("Path:", " -> ".join(path))
        print("Total cost:", ans.cost)
    else:
        print("No path found")

    print("Paths explored:", count)


# graph = {
#     "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
#     "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
#     "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Columbus", 144), ("Pittsburgh", 189)],
#     "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
#     "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
#     "Pittsburgh": [("Cleveland", 189), ("Columbus", 185), ("Buffalo", 215), ("Philadelphia", 305)],
#     "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150)],
#     "Syracuse": [("Buffalo", 150), ("Boston", 312), ("New York", 254)],
#     "Boston": [("Syracuse", 312), ("Providence", 50), ("Portland", 107)],
#     "Providence": [("Boston", 50), ("New York", 181)],
#     "New York": [("Providence", 181), ("Syracuse", 254), ("Philadelphia", 97)],
#     "Philadelphia": [("New York", 97), ("Baltimore", 101), ("Pittsburgh", 305)],
#     "Baltimore": [("Philadelphia", 101)],
#     "Portland": [("Boston", 107)]
# }


# def best_first_search(graph, start, goal):
#     cost = 0
#     priority_queue = [(start, cost, [start])]
#     visited=[]
#     while priority_queue:
#         min = 0
#         for i in range(len(priority_queue)):
#             if priority_queue[0][1] > priority_queue[i][1]:
#                 min = i
#         current_city, cost, path = priority_queue.pop(min)
#         if current_city in visited:
#             continue
#         visited.append(current_city)
#         if current_city == goal:
#             return path, cost
#         for neighbour, distance in graph[current_city]:
#             if neighbour not in visited:
#                 new_cost = cost + distance
#                 new_path = path + [neighbour]
#                 priority_queue.append((neighbour, new_cost, new_path))



#     return None, 0
# path, total_cost = best_first_search(graph, "Syracuse", "Chicago")
# print("Path:", "->".join(path))
# print("Total cost:", total_cost)