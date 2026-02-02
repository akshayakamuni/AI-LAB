# def Simple_Reflex_Vacuum_Cleaner(states, percepts):
import random

rooms = ["A", "B", "C"]

environment = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Dirty"
}


agent_location = "A"

score = 0

print("\n---- RANDOMIZED VACUUM AGENT ----\n")

steps = 15


def Simple_Reflex_Vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    else:
        return random.choice(["MoveLeft", "MoveRight"])


for step in range(steps):

    percept = (agent_location, environment[agent_location])

    action = Simple_Reflex_Vacuum_agent(agent_location, environment[agent_location])

    print(f"Percept: {percept} -> Action: {action}")

   
    if action == "Suck":
        environment[agent_location] = "Clean"
        score -= 1

    elif action == "MoveLeft":
        if environment[agent_location] == "Dirty":
            score -= 5 
        if agent_location == "C":
            agent_location = "B"
        elif agent_location == "B":
            agent_location = "A"
        score -= 1

    elif action == "MoveRight":
        if environment[agent_location] == "Dirty":
            score -= 5 
        if agent_location == "A":
            agent_location = "B"
        elif agent_location == "B":
            agent_location = "C"
        score -= 1

    
    if all(state == "Clean" for state in environment.values()):
        score += 10
        print("\nAll rooms cleaned successfully!")
        break
    # count = 0
    # for state in environment.values():
    #     if state == "Clean":
    #         count += 1
    # if count == len(environment):
    #     score += 10
    #     print("\nAll rooms cleaned successfully!")
    #     break


print("\nFinal Environment:", environment)
print("Final Performance Score:", score)


#without randomization
# rooms = ["A", "B", "C"]


# environment = {
#     "A": "Dirty",
#     "B": "Dirty",
#     "C": "Clean"
# }


# agent_location = "A"


# score = 0

# # Rule Table 
# rules = {
#     ("A", "Dirty"): "Suck",
#     ("B", "Dirty"): "Suck",
#     ("C", "Dirty"): "Suck",

#     ("A", "Clean"): "MoveRight",
#     ("B", "Clean"): "MoveRight",
#     ("C", "Clean"): "MoveLeft"
# }


# def simple_reflex_agent(location, status):
#     return rules[(location, status)]


# print("---- Vacuum Agent Simulation ----\n")

# steps = 10

# for step in range(steps):

#     percept = (agent_location, environment[agent_location])

#     action = simple_reflex_agent(agent_location, environment[agent_location])

#     print(f"Percept: {percept} -> Action: {action}")

#     # Perform action
#     if action == "Suck":
#         environment[agent_location] = "Clean"
#         score -= 1

#     elif action == "MoveRight":
#         if agent_location == "A":
#             agent_location = "B"
#         elif agent_location == "B":
#             agent_location = "C"
#         score -= 1

#     elif action == "MoveLeft":
#         if agent_location == "C":
#             agent_location = "B"
#         elif agent_location == "B":
#             agent_location = "A"
#         score -= 1

    
#     if all(state == "Clean" for state in environment.values()):
#         score += 10
#         print("\nAll rooms are CLEAN!")
#         break

# print("\nFinal Environment:", environment)
# print("Final Score:", score)
