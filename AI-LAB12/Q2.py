# -------- INPUT GRID (0 = empty) --------
grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,8,0,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,7,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,5,0,0,0,0,2]
]

# -------- STEP 1: Create Domains --------
domains = {}

for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            domains[(i,j)] = [1,2,3,4,5,6,7,8,9]
        else:
            domains[(i,j)] = [grid[i][j]]

# -------- STEP 2: Get Neighbors --------
def get_neighbors(cell):
    i, j = cell
    neighbors = set()

    # same row
    for col in range(9):
        if col != j:
            neighbors.add((i, col))

    # same column
    for row in range(9):
        if row != i:
            neighbors.add((row, j))

    # same 3x3 box
    box_i = (i // 3) * 3
    box_j = (j // 3) * 3

    for r in range(box_i, box_i + 3):
        for c in range(box_j, box_j + 3):
            if (r, c) != (i, j):
                neighbors.add((r, c))

    return neighbors

# -------- STEP 3: Create Arcs --------
queue = []

for cell in domains:
    for neighbor in get_neighbors(cell):
        queue.append((cell, neighbor))

# -------- STEP 4: Revise Function --------
def revise(x, y):
    revised = False
    removed_values = []

    for val in domains[x][:]:  # copy list
        # if y has only one value and it is same → remove from x
        if len(domains[y]) == 1 and val == domains[y][0]:
            domains[x].remove(val)
            removed_values.append(val)
            revised = True

    if revised:
        print(f"Revise {x},{y} -> removed {removed_values}")

    return revised

# -------- STEP 5: AC-3 Algorithm --------
def AC3():
    count_removed = 0

    while len(queue) > 0:
        (x, y) = queue.pop(0)

        if revise(x, y):
            count_removed += 1

            if len(domains[x]) == 0:
                return False, count_removed

            for z in get_neighbors(x):
                if z != y:
                    queue.append((z, x))

    return True, count_removed

# -------- RUN AC-3 --------
result, removed = AC3()

# -------- OUTPUT --------
print("\nAC-3 Result:", "Consistent" if result else "Failure")
print("Values removed:", removed)

print("\nRemaining Domain Sizes:")
for i in range(9):
    for j in range(9):
        print(len(domains[(i,j)]), end=" ")
    print()