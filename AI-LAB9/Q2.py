import math

# Graph with costs
graph = {
    "Syracuse": [("Buffalo",150), ("NewYork",254), ("Boston",312)],
    "Buffalo": [("Detroit",256), ("Cleveland",189)],
    "Detroit": [("Chicago",283)],
    "Cleveland": [("Chicago",345)],
    "NewYork": [("Philadelphia",97)],
    "Philadelphia": [("Pittsburgh",305)],
    "Pittsburgh": [("Cleveland",144)],
    "Boston": [("Providence",50)],
    "Providence": []
}

goal_city = "Chicago"


def print_indent(depth):
    for i in range(depth):
        print("  ", end="")


def alphabeta(current_city, depth, is_max_player, alpha, beta, total_cost):

    # Print current node
    print_indent(depth)
    print("Visiting:", current_city, " Cost:", total_cost, " Alpha:", alpha, " Beta:", beta)

    # Goal check
    if current_city == goal_city:
        print_indent(depth)
        print("Goal reached at", current_city, "with cost", total_cost)
        return total_cost

    # Dead end
    if current_city not in graph or len(graph[current_city]) == 0:
        print_indent(depth)
        print("Dead end at", current_city)
        return math.inf

    # MAX player
    if is_max_player:
        best_value = -math.inf

        for next_city, step_cost in graph[current_city]:

            value = alphabeta(next_city,
                              depth + 1,
                              False,
                              alpha,
                              beta,
                              total_cost + step_cost)

            if value > best_value:
                best_value = value

            if best_value > alpha:
                alpha = best_value

            print_indent(depth)
            print("MAX node", current_city, "best =", best_value)

            # Pruning
            if beta <= alpha:
                print_indent(depth)
                print("PRUNING at", current_city)
                break

        return best_value

    # MIN player
    else:
        best_value = math.inf

        for next_city, step_cost in graph[current_city]:

            value = alphabeta(next_city,
                              depth + 1,
                              True,
                              alpha,
                              beta,
                              total_cost + step_cost)

            if value < best_value:
                best_value = value

            if best_value < beta:
                beta = best_value

            print_indent(depth)
            print("MIN node", current_city, "best =", best_value)

            # Pruning
            if beta <= alpha:
                print_indent(depth)
                print("PRUNING at", current_city)
                break

        return best_value


# Run
result = alphabeta("Syracuse", 0, False, -math.inf, math.inf, 0)

print("\nMinimum cost from Syracuse to Chicago:", result)