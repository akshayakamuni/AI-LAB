
MOVES = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(g, b):
    gr = 3 - g
    br = 3 - b
    return (0 <= g <= 3 and 0 <= b <= 3 and (g == 0 or g >= b) and (gr == 0 or gr >= br))

def successors(state):
    g, b, boat = state
    next_states = []

    for move in MOVES:
        dg = move[0]
        db = move[1]

        if boat == 0:   
            ng = g - dg
            nb = b - db
            nb_side = 1
        else:         
            ng = g + dg
            nb = b + db
            nb_side = 0

        if valid(ng, nb):
            next_states.append((ng, nb, nb_side))

    return next_states


def dls(state, limit, path, explored):
    explored.add(state)

    if state == (0, 0, 1):
        return path

    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    children = successors(state)

    for child in children:
        if child not in explored:
            result = dls(child, limit - 1, path + [child], explored)

            if result == "cutoff":
                cutoff_occurred = True
            elif result:
                return result

    if cutoff_occurred:
        return "cutoff"
    else:
        return None


# DLS
explored_dls = set()
result_dls = dls((3,3,0), 3, [(3,3,0)], explored_dls)

print("DLS Result:", result_dls)
print("DLS Explored States:", len(explored_dls))


#IDS
def ids():
    depth = 0

    while True:
        explored = set()
        result = dls((3,3,0), depth, [(3,3,0)], explored)

        print("Depth:", depth, "Explored:", len(explored))

        if result and result != "cutoff":
            return result, explored

        depth += 1


solution, explored_ids = ids()

print("\nIDS Solution Path:")
for step in solution:
    print(step)

print("IDS Explored States:", len(explored_ids))
