# Implement Greedy search algorithm for any of the following application:
# I. Selection Sort
# V. Prim's Minimal Spanning Tree Algorithm

# I. Selection Sort

import heapq

a = [int(input(f"Enter value {i+1}: ")) for i in range(int(input("Total number of elements: ")))]
print("Unsorted Array:", a)

for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print("Selection Sort")
print("Sorted Array:", a)

# V. Prim's Algorithm

def prim(graph, start):
    mst, visited = [], set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for nxt, cost2 in graph[to].items():
                if nxt not in visited:
                    heapq.heappush(edges, (cost2, to, nxt))
    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

print("Prim's Algorithm")
print("Prim's MST:", prim(graph, 'A'))


# =============================================
# ✅ GREEDY ALGORITHMS – THEORETICAL QUESTIONS & ALGORITHMS
# =============================================

# ---------------------------------------------
# I. SELECTION SORT (Greedy Approach)
# ---------------------------------------------

# Q1: Why is Selection Sort greedy?
# A1: It selects the minimum element from unsorted array in each step.

# Q2: Time complexity?
# A2: O(n²) for all cases.

# Q3: Is Selection Sort stable?
# A3: No, it's not.

# Algorithm:
# Step 1: For i = 0 to n - 1:
#     a. Set min_index = i
#     b. For j = i+1 to n:
#         - If a[j] < a[min_index], set min_index = j
#     c. Swap a[i] with a[min_index]
# Step 2: End

# ---------------------------------------------
# II. MINIMUM SPANNING TREE (MST)
# (Covered using Prim's and Kruskal's below)
# ---------------------------------------------

# ---------------------------------------------
# III. SINGLE SOURCE SHORTEST PATH (Dijkstra's)
# ---------------------------------------------

# Q1: What is Dijkstra’s Algorithm?
# A1: It finds shortest path from a source to all nodes using greedy method.

# Q2: Can it work with negative weights?
# A2: No.

# Q3: Time complexity?
# A3: O(E + V log V) using heap.

# Algorithm:
# Step 1: Set distance of source = 0, others = ∞
# Step 2: Add source to priority queue
# Step 3: While queue is not empty:
#     a. Pop vertex with min distance
#     b. For neighbors, update distance if shorter path found
#     c. Push updated neighbors into queue
# Step 4: End

# ---------------------------------------------
# IV. JOB SCHEDULING PROBLEM (Greedy)
# ---------------------------------------------

# Q1: Goal?
# A1: Maximize profit by scheduling jobs within deadlines.

# Q2: Why greedy?
# A2: Highest profit jobs are scheduled first.

# Algorithm:
# Step 1: Sort jobs by descending profit
# Step 2: For each job:
#     a. Find latest free slot before its deadline
#     b. Assign if slot is available
# Step 3: Return total profit & scheduled jobs

# ---------------------------------------------
# V. PRIM’S MINIMAL SPANNING TREE ALGORITHM
# ---------------------------------------------

# Q1: Why is Prim's greedy?
# A1: Always picks the lowest-cost edge connecting to MST.

# Q2: Time complexity?
# A2: O(E log V)

# Algorithm:
# Step 1: Start from any vertex, mark as visited
# Step 2: Add all edges to min-heap
# Step 3: While heap is not empty:
#     a. Pick edge with min weight
#     b. If new vertex not visited:
#         - Add to MST
#         - Push its edges to heap
# Step 4: Repeat until MST complete

# ---------------------------------------------
# VI. KRUSKAL’S MINIMAL SPANNING TREE ALGORITHM
# ---------------------------------------------

# Q1: Difference from Prim's?
# A1: Kruskal’s adds edges in increasing order, avoiding cycles using union-find.

# Q2: Time complexity?
# A2: O(E log E)

# Algorithm:
# Step 1: Sort all edges by weight
# Step 2: Initialize disjoint sets for each vertex
# Step 3: For each edge (u, v):
#     a. If u and v are in different sets:
#         - Add to MST
#         - Union their sets
# Step 4: Stop when MST has V-1 edges

# ---------------------------------------------
# VII. DIJKSTRA’S SHORTEST PATH (Repeat of III)
# ---------------------------------------------

# Already covered above in III.

# =============================================
# SUMMARY: All above problems follow greedy approach by:
# - Selecting the best local option (min cost, max profit, etc.)
# - Hoping it leads to a globally optimal solution
# =============================================
