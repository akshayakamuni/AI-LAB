# Goal state
goal_state = (0,1,2,
              3,4,5,
              6,7,8)

# Start state
start_state = (7,2,4,
               5,0,6,
               8,3,1)

# Possible blank moves
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


def bfs():
    queue = []               # Normal list as queue
    queue.append(start_state)

    visited = set()
    visited.add(start_state)

    explored = 0

    while len(queue) > 0:

        current = queue.pop(0)   # Remove first element (FIFO)
        explored += 1

        if current == goal_state:
            print("Goal Found!")
            print("States Explored (BFS):", explored)
            return

        neighbors = get_neighbors(current)

        for state in neighbors:
            if state not in visited:
                visited.add(state)
                queue.append(state)


bfs()
