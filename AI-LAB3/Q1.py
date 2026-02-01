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


def randomized_agent(location, status):
    if status == "Dirty":
        return "Suck"
    else:
        return random.choice(["MoveLeft", "MoveRight"])


for step in range(steps):

    percept = (agent_location, environment[agent_location])

    action = randomized_agent(agent_location, environment[agent_location])

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
