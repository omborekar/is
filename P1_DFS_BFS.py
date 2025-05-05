# Graph (common for both DFS and BFS)
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F', 'G']),
    'D': set(['B']),
    'E': set(['B']),
    'F': set(['C']),
    'G': set(['C'])
}

# Depth First Search (DFS) - Recursive
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")   # Print the node
        visited.add(node)      # Mark the node as visited
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)  # Recursively visit all neighbors

# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()           # Set to keep track of visited nodes
    queue = [start]           # Initialize queue with the starting node
    
    while queue:
        vertex = queue.pop(0)  # Dequeue the first element
        if vertex not in visited:
            print(vertex, end=" ")  # Print the node
            visited.add(vertex)     # Mark the node as visited
            queue.extend(graph[vertex] - visited)  # Add unvisited neighbors to queue

# Running DFS
print("DFS Traversal starting from B:")
dfs(graph, 'B', set())  # Starting DFS from node 'B'

print("\n")

# Running BFS
print("BFS Traversal starting from A:")
bfs(graph, 'A')  # Starting BFS from node 'A'




# Q1: What is the difference between DFS and BFS?
# A1: DFS uses a stack (or recursion) to explore as deep as possible before backtracking, while BFS uses a queue to explore all neighbors level by level.

# Q2: What data structures are used in DFS and BFS?
# A2: DFS typically uses a stack or recursion and a set for visited nodes, while BFS uses a queue and a set for visited nodes.

# Q3: In what scenarios would you prefer BFS over DFS?
# A3: BFS is preferred when searching for the shortest path in an unweighted graph or when the solution is likely to be close to the root node.

# Q4: When is DFS preferred over BFS?
# A4: DFS is preferred when the solution is likely to be deep in the graph or when memory efficiency is more important.

# Q5: What is the time complexity of DFS and BFS?
# A5: Both have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.

# Q6: What is the space complexity of DFS and BFS?
# A6: DFS has space complexity O(V) due to the recursion stack and visited set. BFS also has O(V) due to the queue and visited set.

# Q7: How does the visited set prevent infinite loops in graphs?
# A7: The visited set keeps track of already visited nodes to avoid revisiting them, which prevents cycles from causing infinite loops.

# Q8: Can DFS and BFS be used for disconnected graphs?
# A8: Yes, but you need to run the algorithm separately for each disconnected component or modify it to cover all nodes.

# Q9: How do DFS and BFS differ in terms of traversal output?
# A9: DFS may go deep into one path before exploring others, leading to depth-based traversal. BFS explores all nodes level by level.

# Q10: Is the traversal order of DFS and BFS always the same for a given graph?
# A10: No, the order depends on the structure of the graph and the order in which neighbors are processed.

# Q11: Can DFS or BFS detect cycles in a graph?
# A11: Yes, both can be modified to detect cycles by checking if a node is revisited that is not the parent in the case of undirected graphs.

# Q12: What happens if we don’t use a visited set in DFS or BFS?
# A12: It may result in infinite loops or redundant processing of the same nodes, especially in graphs with cycles.

# Q13: What kind of graph is used in this program?
# A13: The graph is an undirected graph represented using an adjacency list with sets.

# Q14: What will be the output of DFS starting from node 'B'?
# A14: Output depends on the order of neighbors in the set but generally: B A C F G D E or another valid depth-first traversal.

# Q15: What will be the output of BFS starting from node 'A'?
# A15: Output depends on neighbor ordering but generally: A B C D E F G or another valid breadth-first traversal.
