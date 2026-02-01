

def level_crossing_agent(inbound, outbound, obstacle, emergency):

    
    if emergency == "Active":
        return ("Lower Gate", "Red Signal", "Hooter On")

    
    if (inbound == "TrainDetected" or outbound == "TrainDetected") and obstacle == "Blocked":
        return ("Lower Gate", "Red Signal", "Hooter On")

    
    if (inbound == "TrainDetected" or outbound == "TrainDetected") and obstacle == "Clear":
        return ("Lower Gate", "Green Signal", "Hooter On")

    
    if inbound == "NoTrain" and outbound == "NoTrain" and obstacle == "Clear":
        return ("Raise Gate", "Green Signal", "Hooter Off")

    return ("Hold State", "Hold Signal", "Hooter Off")



test_cases = [
    ("NoTrain", "NoTrain", "Clear", "Neutral"),
    ("TrainDetected", "NoTrain", "Clear", "Neutral"),
    ("TrainDetected", "NoTrain", "Blocked", "Neutral"),
    ("NoTrain", "NoTrain", "Blocked", "Active")
]

print("\n---- LEVEL CROSSING SIMULATION ----\n")

for case in test_cases:

    inbound, outbound, obstacle, emergency = case

    action = level_crossing_agent(inbound, outbound, obstacle, emergency)

    print("Percept:",
          case,
          "=> Action:",
          action)
