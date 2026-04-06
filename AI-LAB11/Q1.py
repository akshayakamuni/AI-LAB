
# Districts 
districts = [
    "Kuchchh", "Banaskantha", "Patan", "Mehsana", "Sabarkantha",
    "Gandhi Nagar", "Ahmedabad", "Surendranagar", "Kheda", "Anand",
    "Panchmahal", "Dahod", "Vadodara", "Jamnagar", "Rajkot",
    "Porbandar", "Amreli", "Junaghad", "Bhavnagar", "Bharuch",
    "Narmada", "Surat", "Dangs", "Navsari", "Valsad"
]

# Adjacency list 
adjacency = {
    "Kuchchh":       ["Banaskantha", "Patan", "Surendranagar", "Rajkot"],
    "Banaskantha":   ["Kuchchh", "Patan", "Mehsana", "Sabarkantha"],
    "Patan":         ["Kuchchh", "Banaskantha", "Mehsana", "Surendranagar"],
    "Mehsana":       ["Banaskantha", "Patan", "Sabarkantha", "Gandhi Nagar", "Ahmedabad", "Surendranagar"],
    "Sabarkantha":   ["Banaskantha", "Mehsana", "Gandhi Nagar","Kheda", "Panchmahal"],
    "Gandhi Nagar":  ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],
    "Ahmedabad":     ["Mehsana", "Gandhi Nagar", "Surendranagar", "Kheda", "Anand"],
    "Surendranagar": ["Kuchchh", "Patan", "Mehsana", "Ahmedabad", "Rajkot", "Bhavnagar", "Anand"],
    "Kheda":         ["Gandhi Nagar", "Sabarkantha","Ahmedabad", "Anand", "Panchmahal", "Vadodara"],
    "Anand":         ["Ahmedabad", "Surendranagar", "Kheda", "Vadodara", "Bharuch"],
    "Panchmahal":    ["Sabarkantha", "Kheda", "Vadodara", "Dahod"],
    "Dahod":         ["Panchmahal", "Vadodara"],
    "Vadodara":      ["Kheda", "Anand", "Panchmahal", "Dahod", "Bharuch", "Narmada"],
    "Jamnagar":      ["Kuchchh", "Rajkot", "Porbandar"],
    "Rajkot":        ["Kuchchh", "Jamnagar", "Surendranagar", "Porbandar", "Amreli", "Junaghad", "Bhavnagar"],
    "Porbandar":     ["Jamnagar", "Rajkot", "Junaghad"],
    "Amreli":        ["Rajkot", "Junaghad", "Bhavnagar"],
    "Junaghad":      ["Porbandar", "Amreli", "Rajkot"],
    "Bhavnagar":     ["Surendranagar", "Amreli", "Rajkot", "Ahmedabad"],
    "Bharuch":       ["Anand", "Vadodara", "Narmada", "Surat"],
    "Narmada":       ["Vadodara", "Bharuch", "Surat"],
    "Surat":         ["Bharuch", "Narmada", "Dangs", "Navsari"],
    "Dangs":         ["Surat", "Navsari"],
    "Navsari":       ["Surat", "Dangs", "Valsad"],
    "Valsad":        ["Navsari"],
}

COLORS = ["Red", "Green", "Blue", "Yellow"]

def is_valid(district, color, assignment):
    """Check if assigning color to district violates any constraint."""
    for neighbor in adjacency[district]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtrack(assignment, districts):
    """Recursive backtracking CSP solver."""
    if len(assignment) == len(districts):
        return assignment  # All districts colored — solution found

    # Pick the next unassigned district 
    unassigned = [d for d in districts if d not in assignment]
    district = unassigned[0]

    for color in COLORS:
        if is_valid(district, color, assignment):
            assignment[district] = color
            result = backtrack(assignment, districts)
            if result:
                return result
            del assignment[district]  # Backtrack

    return None  # No valid color found — trigger backtrack

def solve():
    solution = backtrack({}, districts)
    if solution:
        print("Solution found!\n")
        # Group districts by color
        color_groups = {}
        for district, color in solution.items():
            color_groups.setdefault(color, []).append(district)

        for color, group in sorted(color_groups.items()):
            print(f"{color} ({len(group)} districts):")
            for d in group:
                print(f"  - {d}")
            print()

        # Verify no two adjacent districts share a color
        print("Verifying constraints...")
        valid = True
        for district, color in solution.items():
            for neighbor in adjacency[district]:
                if solution.get(neighbor) == color:
                    print(f"  CONFLICT: {district} and {neighbor} both have {color}!")
                    valid = False
        if valid:
            print("All constraints satisfied. Valid coloring!")
    else:
        print("No solution found.")

solve()
