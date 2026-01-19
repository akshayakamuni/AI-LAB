from collections import deque

# Adjacency list
graph = {
    "Raj": ["Sunil", "NehaOrange"],
    "Priya": ["Raj", "Aarav", "Akash"],
    "Aarav": ["NehaOrange", "NehaPink", "ArjunMan"],
    "Sunil": ["Sneha", "Maya", "Akash", "Raj"],
    "Akash": ["Sunil", "Priya"],
    "NehaOrange": ["Akash", "Aarav", "Raj", "Sneha"],
    "NehaPink": ["NehaOrange", "Rahul", "Priya", "Aarav", "ArjunMan"],
    "Sneha": ["Rahul", "Maya", "Sunil", "NehaOrange"],
    "Rahul": ["Sneha", "NehaPink", "NehaOrange", "ArjunMan", "Pooja"],
    "ArjunMan": ["NehaPink", "Rahul", "Aarav"],
    "Maya": ["Sunil", "Rahul","Sneha", "ArjunChild"],
    "ArjunChild": ["Pooja", "Maya"],
    "Pooja": ["ArjunMan", "ArjunChild", "Rahul"]
}

# BFS
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    print("BFS Tree (Parent -> Child):")
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                print(f"{u} -> {v}")

# DFS
def dfs(graph, start):
    visited = set()
    print("\nDFS Tree (Parent -> Child):")
    dfs_util(graph, start, visited)

def dfs_util(graph, u, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            print(f"{u} -> {v}")
            dfs_util(graph, v, visited)

start_node = "Rahul"
bfs(graph, start_node)
dfs(graph, start_node)