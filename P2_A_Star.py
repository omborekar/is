# Implement A star Algorithm for any game search problem.

# Simple Implementation of A* 

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 1, 'G': 0
}

def a_star(start, goal):
    open_list = {start}
    g = {start: 0}
    parents = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: g[x] + heuristic[x])  # Get node with lowest cost
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Return the path from start to goal

        open_list.remove(current)
        for neighbor, cost in graph[current].items():
            temp_g = g[current] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                parents[neighbor] = current
                open_list.add(neighbor)

    return None

# Run A* from A to G
print("Path:", a_star('A', 'G'))


# ---------------------------------------Use Only One-------------------------------------------------


# Implemented A* using game

# Maze: 0 = open, 1 = wall
maze = [
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

start = (0, 0)
goal = (3, 1)

rows = len(maze)
cols = len(maze[0])

# Heuristic: Manhattan distance to goal
def h(cell):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def a_star():
    open_list = [start]
    came_from = {}
    cost = {start: 0}

    while open_list:
        current = min(open_list, key=lambda c: cost[c] + h(c))

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        open_list.remove(current)

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            next_cell = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                new_cost = cost[current] + 1
                if next_cell not in cost or new_cost < cost[next_cell]:
                    cost[next_cell] = new_cost
                    came_from[next_cell] = current
                    if next_cell not in open_list:
                        open_list.append(next_cell)

    return None

# Run the A* algorithm
path = a_star()
print("Path from start to goal:", path)



# Q1: What is the A* algorithm?
# A1: A* is a best-first search algorithm that finds the shortest path from a start node to a goal node using a combination of actual cost (g) and heuristic cost (h).

# Q2: What is the evaluation function used in A*?
# A2: The evaluation function is f(n) = g(n) + h(n), where g(n) is the cost from start to node n, and h(n) is the heuristic estimate from n to goal.

# Q3: What is a heuristic?
# A3: A heuristic is an estimate of the cost from the current node to the goal node, used to guide the search efficiently.

# Q4: What makes a heuristic admissible?
# A4: A heuristic is admissible if it never overestimates the actual cost to reach the goal from any node.

# Q5: What is the time complexity of the A* algorithm?
# A5: In the worst case, the time complexity is exponential, but it performs better than uninformed search if the heuristic is good.

# Q6: What data structures are used in A*?
# A6: A* typically uses an open list (e.g., a set or priority queue), a closed list (optional), a cost dictionary, and a parent tracking dictionary.

# Q7: How does A* differ from Dijkstra’s Algorithm?
# A7: Dijkstra’s considers only g(n) (actual cost), while A* adds h(n) (heuristic), making it more efficient with a good heuristic.

# Q8: What is the role of the `g` dictionary in this code?
# A8: It stores the cost of the shortest path found so far from the start node to each node.

# Q9: Why do we use `min(open_list, key=lambda x: g[x] + heuristic[x])`?
# A9: To select the node with the lowest estimated total cost to reach the goal.

# Q10: What happens if the heuristic is 0 for all nodes?
# A10: A* behaves like Dijkstra’s Algorithm and explores all possible paths based on actual cost.

# Q11: What is the purpose of the `parents` dictionary?
# A11: It keeps track of the path by storing each node's predecessor for backtracking once the goal is found.

# Q12: What is Manhattan distance, and why is it used in the maze version?
# A12: Manhattan distance is the sum of the absolute differences of the coordinates; it's suitable for grid-based movement without diagonals.

# Q13: What is the significance of checking bounds in the maze version?
# A13: It ensures we don’t access invalid cells outside the maze boundaries.

# Q14: Why do we check if `maze[nx][ny] == 0`?
# A14: To ensure that we only move to open (walkable) cells, not walls (which are marked as 1).

# Q15: What happens if there is no path from start to goal?
# A15: The algorithm will return `None` if the goal is not reachable.

# Q16: Can A* be used on weighted graphs with negative weights?
# A16: No, A* (like Dijkstra’s) assumes non-negative weights for correctness.

# Q17: What is the output of the algorithm?
# A17: A list representing the shortest path from the start node to the goal node.

# Q18: How is A* optimal and complete?
# A18: A* is complete and optimal if the heuristic is admissible and consistent.

# Q19: Why do we use sets or lists for the open list?
# A19: To track which nodes are to be explored next; sets provide fast lookup, while lists are easier for ordered processing.

# Q20: How can A* be optimized further?
# A20: By using a priority queue (e.g., heapq) for the open list to reduce the cost of finding the minimum f(n).


# A* Algorithm (General Form):

# Step 1: Initialize
# - Open list (priority queue or list) with the start node.
# - Closed list (optional) to store visited nodes.
# - g(start) = 0 (cost from start to start is 0).
# - f(start) = g(start) + h(start), where h is the heuristic.
# - Initialize parent dictionary to reconstruct path.

# Step 2: Loop until open list is empty:
#   a. Select the node ‘current’ from the open list with the lowest f(n) = g(n) + h(n).
#   b. If current is the goal node:
#       - Reconstruct the path using the parent dictionary.
#       - Return the path and exit.
#   c. Remove current from the open list.
#   d. For each neighbor of current:
#       i. Calculate tentative_g = g(current) + cost to neighbor.
#       ii. If neighbor is not in g or tentative_g < g(neighbor):
#           - Update g(neighbor) = tentative_g
#           - Update f(neighbor) = g(neighbor) + h(neighbor)
#           - Set parent[neighbor] = current
#           - Add neighbor to open list if not already present.

# Step 3: If goal is not reached and open list is empty:
#   - Return failure (no path exists).
