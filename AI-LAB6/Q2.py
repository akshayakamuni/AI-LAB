maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

def astar_all_rewards(maze):

    rows = 5
    cols = 5

    # Find start
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 2:
                start = (i, j)

    # Find rewards
    rewards = []
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 3:
                rewards.append((i, j))

    current_position = start
    total_path = []
    visited_tiles = []

    # Manhattan heuristic
    def heuristic(pos, goals):
        min_dist = float('inf')
        for goal in goals:
            dist = abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
            min_dist = min(min_dist, dist)
        return min_dist

    directions = [(0,-1), (0,1), (-1,0), (1,0)]

    # Collect rewards one by one
    while len(rewards) > 0:

        print("\n==============================")
        print("Starting A* from:", current_position)
        print("Remaining Rewards:", rewards)
        print("==============================\n")

        open_list = []
        open_list.append([current_position, [current_position], 0])

        g_cost = {}
        g_cost[current_position] = 0

        found_goal = None
        path_to_goal = []

        while len(open_list) > 0:

            # Select node with smallest f(n)
            smallest = 0
            for i in range(len(open_list)):
                pos = open_list[i][0]
                f1 = g_cost[pos] + heuristic(pos, rewards)

                pos_small = open_list[smallest][0]
                f2 = g_cost[pos_small] + heuristic(pos_small, rewards)

                if f1 < f2:
                    smallest = i

            selected_pos = open_list[smallest][0]
            selected_g = g_cost[selected_pos]
            selected_h = heuristic(selected_pos, rewards)
            selected_f = selected_g + selected_h

            print("Selected Node:", selected_pos,
                  " g(n):", selected_g,
                  " h(n):", selected_h,
                  " f(n):", selected_f)

            current = selected_pos
            path = open_list[smallest][1]
            cost = open_list[smallest][2]

            open_list.pop(smallest)

            if current not in visited_tiles:
                visited_tiles.append(current)

            # If reward found
            if current in rewards:
                print(">>> Reward Found at:", current)
                found_goal = current
                path_to_goal = path
                break

            # Expand neighbors
            for d in directions:
                new_r = current[0] + d[0]
                new_c = current[1] + d[1]

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if maze[new_r][new_c] != 1:

                        new_pos = (new_r, new_c)
                        new_cost = cost + 1

                        if new_pos not in g_cost or new_cost < g_cost[new_pos]:
                            g_cost[new_pos] = new_cost

                            h_value = heuristic(new_pos, rewards)
                            f_value = new_cost + h_value

                            print("   Generated:",
                                  new_pos,
                                  " g(n):", new_cost,
                                  " h(n):", h_value,
                                  " f(n):", f_value)

                            open_list.append([new_pos, path + [new_pos], new_cost])

        total_path += path_to_goal
        current_position = found_goal
        rewards.remove(found_goal)

    return total_path, visited_tiles


# Run
path, visited = astar_all_rewards(maze)

print("\n===================================")
print("Final Path to Collect All Rewards:")
print(path)

print("\nTiles Visited:")
print(visited)