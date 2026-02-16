class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, cost):
        self.queue.append((cost, item))

    def pop(self):
        # find minimum cost item
        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i

        cost, item = self.queue.pop(min_index)
        return cost, item

    def is_empty(self):
        return len(self.queue) == 0


def uniform_cost_search(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    pq = PriorityQueue()
    pq.push(start, 0)

    reached = {start: 0}
    parent = {}

    while not pq.is_empty():

        cost, current = pq.pop()

        if current == goal:
            
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, cost

        x, y = current

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:

                new_cost = cost + 1
                neighbor = (nx, ny)

                if neighbor not in reached or new_cost < reached[neighbor]:
                    reached[neighbor] = new_cost
                    parent[neighbor] = current
                    pq.push(neighbor, new_cost)

    return None, float("inf")


grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,1,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

start = (0,0)
goal = (4,4)

path, cost = uniform_cost_search(grid, start, goal)

print("Evacuation path:", path)
print("Total cost:", cost)
