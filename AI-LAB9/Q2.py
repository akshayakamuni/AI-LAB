import math

# Graph with step costs (miles)
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

goal = "Chicago"


def alphabeta(city, depth, isMax, alpha, beta, cost_so_far):

    if city == goal:
        return cost_so_far

    # If no more neighbors
    if city not in graph or len(graph[city]) == 0:
        return math.inf


    if isMax:
        best = -math.inf

        for next_city, cost in graph[city]:

            val = alphabeta(next_city, depth+1, False,
                            alpha, beta, cost_so_far + cost)

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for next_city, cost in graph[city]:

            val = alphabeta(next_city, depth+1, True,
                            alpha, beta, cost_so_far + cost)

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best


result = alphabeta("Syracuse",0,False,-math.inf,math.inf,0)

print("Minimum cost from Syracuse to Chicago:",result)