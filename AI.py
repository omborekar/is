# ============================
# Group A: DFS and BFS
# ============================

# Q1: What is Depth First Search (DFS)?
# A1: DFS explores each branch as deeply as possible before backtracking. It uses a stack or recursion.

# Q2: What is Breadth First Search (BFS)?
# A2: BFS explores all neighbors at the current depth before moving to the next level. It uses a queue.

# Q3: What is the time complexity of DFS and BFS?
# A3: Both have time complexity O(V + E), where V is vertices and E is edges.

# Q4: When is DFS preferred over BFS?
# A4: DFS is preferred when the solution is likely to be far from the root or depth is more important.

# Q5: When is BFS preferred over DFS?
# A5: BFS is better for finding the shortest path in unweighted graphs.

# Q6: Why use recursion for DFS?
# A6: Because recursion mimics the stack-based behavior of DFS naturally.

# Q7: Can BFS be implemented recursively?
# A7: It's not efficient or common to do so; BFS is best implemented using an explicit queue.

# Q8: How to detect a cycle using DFS?
# A8: If you visit an already visited node that is not the parent, a cycle exists (for undirected graphs).

# Q9: How does DFS work in disconnected graphs?
# A9: Run DFS for each unvisited node in the graph to ensure complete traversal.

# Q10: What is the output of DFS and BFS for the same graph?
# A10: The order may differ, as DFS explores deep while BFS explores wide.


# ============================
# Group A: A* Algorithm
# ============================

# Q11: What is the purpose of the A* algorithm?
# A11: It finds the shortest path from a start node to a goal node using cost and heuristic.

# Q12: What is the formula used in A*?
# A12: f(n) = g(n) + h(n), where g = cost so far, h = estimated cost to goal.

# Q13: What makes a good heuristic in A*?
# A13: A heuristic should be admissible (never overestimate) and consistent (triangle inequality).

# Q14: What happens if the heuristic is zero in A*?
# A14: A* behaves like Dijkstra's algorithm.

# Q15: What is the time complexity of A*?
# A15: In the worst case, it's exponential, but performance depends on the heuristic quality.

# Q16: In what types of problems is A* commonly used?
# A16: Pathfinding in games, robotics, and map routing applications.


# ============================
# Group B: Greedy Algorithms
# ============================

# Q17: What is a greedy algorithm?
# A17: An algorithm that makes locally optimal choices at each step with the hope of finding a global optimum.

# Q18: Why does Selection Sort use a greedy strategy?
# A18: It selects the smallest element from the unsorted part and moves it to the sorted part at each step.

# Q19: What is the difference between Prim’s and Kruskal’s MST algorithm?
# A19: Prim’s grows from a single vertex; Kruskal’s picks smallest edges and uses union-find to avoid cycles.

# Q20: How does Dijkstra’s algorithm work?
# A20: It uses a priority queue to repeatedly select the closest unvisited vertex and update neighbors.

# Q21: Is Dijkstra's algorithm greedy or dynamic programming?
# A21: It is greedy because it always picks the node with the smallest tentative distance.

# Q22: What kind of problems does the Job Scheduling Algorithm solve?
# A22: It solves optimization problems like maximizing jobs completed before deadlines or minimizing cost.

# Q23: Can greedy algorithms solve all optimization problems?
# A23: No, only those that have the greedy choice property and optimal substructure.


# ============================
# Group B: Constraint Satisfaction Problem (CSP)
# ============================

# Q24: What is a CSP?
# A24: A problem where variables must be assigned values under certain constraints.

# Q25: What is the N-Queens problem?
# A25: Place N queens on an N×N chessboard so that no two queens threaten each other.

# Q26: How does backtracking help solve N-Queens?
# A26: It incrementally builds candidates and backtracks when a violation occurs.

# Q27: How is branch and bound different from backtracking?
# A27: Branch and bound prunes branches using cost bounds; backtracking prunes using feasibility.

# Q28: What is graph coloring in CSP?
# A28: Assigning colors to nodes such that no two adjacent nodes share the same color.

# Q29: What are real-life examples of CSPs?
# A29: Exam scheduling, map coloring, Sudoku, and resource allocation.


# ============================
# Group C: Chatbot
# ============================

# Q30: What is a chatbot?
# A30: A software that interacts with users via text or voice using rules or AI.

# Q31: What are rule-based chatbots?
# A31: Bots that rely on fixed rules and pattern matching (e.g., "if input contains 'price', reply with price info").

# Q32: What are AI-based chatbots?
# A32: Bots that use machine learning and NLP to understand and respond flexibly.

# Q33: What is intent recognition in chatbots?
# A33: Determining what the user wants based on their message (e.g., book ticket, get price, etc.)

# Q34: How can Python help build a chatbot?
# A34: Python offers libraries like NLTK, Rasa, and simple I/O for building chatbots easily.


# ============================
# Group C: Expert System
# ============================

# Q35: What is an expert system?
# A35: A computer system that mimics human decision-making using rules and logic.

# Q36: What are components of an expert system?
# A36: Knowledge base (facts and rules), inference engine (logic), and user interface.

# Q37: Where are expert systems used?
# A37: Medical diagnosis, stock market analysis, scheduling, help desks, and performance evaluation.

# Q38: What is forward chaining?
# A38: A reasoning method that starts with known facts and applies rules to reach conclusions.

# Q39: What is backward chaining?
# A39: Starts from a goal and works backward to check if data supports it.

# Q40: How do you represent knowledge in an expert system?
# A40: Using IF-THEN rules, semantic networks, or frames.
