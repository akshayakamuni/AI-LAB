import random

# State: (location, A, B)
# location: 'A' or 'B'
# A, B: 'Dirty' or 'Clean'

def is_goal(state):
    return state[1] == 'Clean' and state[2] == 'Clean'


def actions(state):
    return ['SUCK', 'LEFT', 'RIGHT']


def results(state, action):
    loc, A, B = state

    outcomes = []

    if action == 'SUCK':
        if loc == 'A':
            # Erratic behavior
            new_A = 'Clean'
            new_B = 'Clean' if random.random() < 0.5 else B
            outcomes.append((loc, new_A, new_B))

            if A == 'Clean' and random.random() < 0.3:
                outcomes.append((loc, 'Dirty', B))

        else:
            new_B = 'Clean'
            new_A = 'Clean' if random.random() < 0.5 else A
            outcomes.append((loc, new_A, new_B))

            if B == 'Clean' and random.random() < 0.3:
                outcomes.append((loc, A, 'Dirty'))

    elif action == 'LEFT':
        outcomes.append(('A', A, B))

    elif action == 'RIGHT':
        outcomes.append(('B', A, B))

    return outcomes


def and_or_search(state, path):
    if is_goal(state):
        return []

    if state in path:
        return None

    for action in actions(state):
        plans = []
        success = True

        for result_state in results(state, action):
            plan = and_or_search(result_state, path + [state])
            if plan is None:
                success = False
                break
            plans.append(plan)

        if success:
            return [action, plans]

    return None


# Initial state
initial_state = ('A', 'Dirty', 'Dirty')

plan = and_or_search(initial_state, [])
print("Generated Plan:")
print(plan)