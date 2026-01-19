# DFS implementation

# Goal state
goal_state = (0,1,2,
              3,4,5,
              6,7,8)

# Start state
start_state = (7,2,4,
               5,0,6,
               8,3,1)

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def get_neighbors(state):
    neighbors = []

    index = state.index(0)
    row = index // 3
    col = index % 3

    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with neighbor
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]

            neighbors.append(tuple(new_state))

    return neighbors

def dfs():
    stack = [start_state]
    visited = set()
    visited.add(start_state)

    explored = 0

    while stack:
        current = stack.pop()
        explored += 1

        if current == goal_state:
            print("Goal Found!")
            print("DFS States Explored:", explored)
            return

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

dfs()
