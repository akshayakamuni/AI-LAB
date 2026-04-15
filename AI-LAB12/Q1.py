projects = ["p1", "p2", "p3", "p4", "p5", "p6"]

conflicts = {
    "p1" : ["p2", "p3", "p6"],
    "p2" : ["p1", "p3", "p4"],
    "p3" : ["p1", "p2", "p5"],
    "p4" : ["p2", "p6"],
    "p5" : ["p3", "p6"],
    "p6" : ["p1", "p4", "p5"]
}

rooms = ["R1", "R2", "R3"]

domains = {p: rooms[:] for p in projects}

queue = []

def arcs(project, conflicts):
    for c in conflicts[project]:
        queue.append((project, c))

for p in projects:
    arcs(p, conflicts)

def revise(x1, x2):
    revised = False
    removed = []

    for r in domains[x1][:]:
        # constraint: x1 != x2
        if all(r == r2 for r2 in domains[x2]):
            domains[x1].remove(r)
            removed.append(r)
            revised = True

    if revised:
        print(f"Revise({x1},{x2}) -> removed {removed}, new domain[{x1}] = {domains[x1]}")
    else:
        print(f"Revise({x1},{x2}) -> no change")

    return revised

def AC_3(queue, conflicts):
    step = 1
    while queue:
        x1, x2 = queue.pop(0)
        print(f"\nStep {step}: Checking arc ({x1}, {x2})")

        if revise(x1, x2):
            if len(domains[x1]) == 0:
                print("Domain wiped out → Failure ")
                return False

            for x3 in conflicts[x1]:
                if x3 != x2:
                    queue.append((x3, x1))

        step += 1

    return True

# Run AC-3
if AC_3(queue, conflicts):
    print("\nAC-3 finished: Arc-consistent")
    print("Final Domains:", domains)
else:
    print("\nNo solution possible")


# projects = ["p1", "p2", "p3", "p4", "p5", "p6"]
# conflicts = {
#     "p1" : ["p2", "p3", "p6"],
#     "p2" : ["p1", "p3", "p4"],
#     "p3" : ["p1", "p2", "p5"],
#     "p4" : ["p2", "p6"],
#     "p5" : ["p3", "p6"],
#     "p6" : ["p1", "p4", "p5"]
# }
# rooms = ["R1", "R2", "R3"]
# queue = []
# def arcs(projects, conflicts):
#     for c in conflicts[projects]:
#         queue.append((projects, c))
# for p in projects:
#     arcs(p, conflicts)

# def AC_3(queue, conflicts):
#     while queue:
#        x1,x2 = queue.pop(0)
#        if revise(x1, x2):
#            if len(conflicts[x1]) == 0:
#                return False
#            for x3 in conflicts[x1]:
#                if x3 != x2:
#                    queue.append((x3, x1))
#     return True
# def revise(x1, x2):
#     revised = False
#     for r in rooms:
#         if r in conflicts[x1] and r in conflicts[x2]:
#             conflicts[x1].remove(r)
#             revised = True
#     return revised
# if AC_3(queue, conflicts):
#     print("Solution exists!")
# else:
#     print("No solution possible.")

