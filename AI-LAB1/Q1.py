from queue import Queue
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


from collections import deque

def bfs_all_paths(graph, start, goal):
    queue = deque([(start, [start], 0)])
    paths = []

    while queue:
        current, path, cost = queue.popleft()

        if current == goal:
            paths.append((path, cost))
            continue

        for neighbour, weight in graph[current]:
            if neighbour not in path:
                queue.append((neighbour, path + [neighbour], cost + weight))

    return paths
# def bfs_all_paths(graph, start, goal):
#     queue = Queue()
#     paths = []

#     queue.enqueue((start, [start], 0))
#     paths.append(start)
#     while queue:
#         c = queue.dequeue()
#         current, path, cost = c[0], c[1], c[2]

#         if current == goal:
#             paths.append((path, cost))
#             continue

#         for neighbour, weight in graph[current]:
#             if neighbour not in path:
#                 queue.enqueue((neighbour, path + [neighbour], cost + weight))

#     return paths
def dfs_all_paths(graph, current, goal, path, cost, paths):
    if current == goal:
        paths.append((path, cost))
        return

    for neighbour, weight in graph[current]:
        if neighbour not in path:
            dfs_all_paths(
                graph,
                neighbour,
                goal,
                path + [neighbour],
                cost + weight,
                paths
            )

def dfs_wrapper(graph, start, goal):
    paths = []
    dfs_all_paths(graph, start, goal, [start], 0, paths)
    return paths
start = "Syracuse"
goal = "Chicago"

print("BFS Paths:")
bfs_paths = bfs_all_paths(graph, start, goal)
for p, c in bfs_paths:
    print(p, "Cost:", c)

print("\nDFS Paths:")
dfs_paths = dfs_wrapper(graph, start, goal)
for p, c in dfs_paths:
    print(p, "Cost:", c)
