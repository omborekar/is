# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound andBacktracking for n-queens problem or a graph coloring problem.

N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]

def is_attack(row, col):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True
    for i in range(N):
        for j in range(N):
            if abs(row - i) == abs(col - j) and board[i][j] == 1:
                return True
    return False

def solve_n_queens(n):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not is_attack(i, j):
                board[i][j] = 1
                if solve_n_queens(n - 1):
                    return True
                board[i][j] = 0
    return False

if solve_n_queens(N):
    print("Solution for the N-Queens Problem:")
    for row in board:
        print(row)
else:
    print("No solution exists.")


# The code solves the N-Queens problem, where the task is to place N queens on an N x N chessboard such that no two queens attack each other.

# It first takes the number of queens (`N`) as input.
# Then, it creates an empty chessboard of size `N x N`.
# The `is_attack()` function checks if placing a queen at a specific position would result in an attack.
# The `solve_n_queens()` function uses **backtracking** to try placing queens one by one:
# It places a queen in an empty spot, then recursively tries to place the next queen.
# If a valid arrangement is found, it prints the board. If not, it backtracks and tries a different arrangement.
#  The program outputs the solution if one exists or says "No solution exists."

def print_board(board):
    for row in board:
        print(" ".join('Q' if col == 1 else '.' for col in row))
    print()

def is_attack(board, row, col, N):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return True

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return True
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return True
        i += 1
        j -= 1

    return False

def solve_n_queens(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if not is_attack(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, N):
                return True
            board[i][col] = 0  # backtrack

    return False

# Main execution
if __name__ == "__main__":
    N = int(input("Enter the number of queens: "))
    board = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        board.append(row)

    if solve_n_queens(board, 0, N):
        print("One possible solution:")
        print_board(board)
    else:
        print("No solution exists.")

# ================================================
# ✅ THEORETICAL QUESTIONS ABOUT CSP (CONSTRAINT SATISFACTION PROBLEMS)
# ================================================

# Q1: What is a Constraint Satisfaction Problem (CSP)?
# A1: A CSP is a problem where the objective is to find values for variables that satisfy a set of constraints. 
# The problem consists of a set of variables, a domain for each variable, and a set of constraints that specify 
# which combinations of values are acceptable.

# Q2: What are the components of a CSP?
# A2: The components of a CSP include:
# - **Variables**: The elements that need to be assigned values.
# - **Domains**: The set of possible values each variable can take.
# - **Constraints**: The conditions that must be satisfied for a solution to be valid.

# Q3: How do CSPs differ from other optimization problems?
# A3: In CSPs, the goal is to find any solution that satisfies the constraints, while in optimization problems, 
# the goal is to find the best solution according to a certain objective function, which may not necessarily be 
# subject to constraints.

# Q4: What is a **backtracking** approach in CSP?
# A4: Backtracking is a **search algorithm** that tries to build a solution incrementally by assigning values to 
# variables one by one, and it **backtracks** when it finds that a partial assignment cannot be extended to a valid solution.

# Q5: What is a **Branch and Bound** approach in CSP?
# A5: Branch and Bound is a method for solving optimization problems. It works by dividing the problem into smaller 
# subproblems (branching) and discarding branches of the search tree that cannot possibly lead to an optimal solution (bounding).

# Q6: How is **constraint propagation** used in CSP?
# A6: Constraint propagation is a technique used to reduce the search space by enforcing constraints during 
# the process of variable assignment. It removes values from a variable's domain that are inconsistent with other variables' domains.

# Q7: What are some **types of constraints** in CSP?
# A7: Constraints can be:
# - **Unary**: Constraints involving a single variable.
# - **Binary**: Constraints involving two variables.
# - **Higher-order**: Constraints involving more than two variables.

# Q8: What is **arc-consistency** in CSP?
# A8: A CSP is arc-consistent if, for every variable, all of its values satisfy the constraints with respect to all other variables. 
# It helps reduce the search space by eliminating values that cannot possibly participate in any valid solution.

# Q9: What is the **backtracking search algorithm** for solving a CSP?
# A9: The backtracking search algorithm assigns values to variables one by one and backtracks when a variable assignment 
# leads to a conflict (i.e., it violates the constraints). It explores all possible assignments to find a valid solution.

# Q10: What is **forward checking** in CSP?
# A10: Forward checking is a technique used to avoid future conflicts by removing values from the domains of unassigned 
# variables as soon as a variable is assigned a value, ensuring that no future assignments will violate any constraints.

# Q11: What is **local search** in the context of CSP?
# A11: Local search algorithms, like **min-conflicts**, are used to iteratively make local changes to a solution to reduce 
# conflicts until a valid solution is found. They are often used in large CSPs where exhaustive search is impractical.

# Q12: What is a **constraint graph** in CSP?
# A12: A constraint graph represents the CSP with variables as nodes and constraints as edges between variables. 
# A constraint is represented as an edge between two variables if the constraint involves both variables.

# Q13: What is **backtracking with constraint propagation**?
# A13: Backtracking with constraint propagation uses constraint propagation techniques (like arc-consistency) to reduce 
# the domains of variables during the search process, which helps to reduce the size of the search space and improve efficiency.

# Q14: What is the **difference between CSP and SAT (Satisfiability) problems**?
# A14: While both CSP and SAT are decision problems, CSP involves assigning values to variables under constraints, 
# while SAT involves finding a truth assignment for variables in a boolean formula such that the formula is true.

# Q15: How can CSPs be represented graphically?
# A15: CSPs can be represented using a **constraint graph**, where each node represents a variable, and edges represent constraints 
# between variables. The search process involves exploring this graph to find assignments that satisfy all the constraints.
# ================================================
# ✅ QUESTIONS SPECIFIC TO N-QUEENS PROBLEM (AS A CSP)
# ================================================

# Q1: How can the N-Queens problem be modeled as a CSP?
# A1: The N-Queens problem can be modeled as a CSP by defining:
# - **Variables**: The columns of the chessboard (one variable per column).
# - **Domains**: The possible row positions (1 through N) for each queen in the column.
# - **Constraints**: 
#     - No two queens should be in the same row.
#     - No two queens should be in the same diagonal.
#     - No two queens should be in the same column.

# Q2: How does the backtracking algorithm solve the N-Queens problem?
# A2: The backtracking algorithm places queens in one column at a time, checking for conflicts. If a conflict is found, 
# it backtracks to the previous column and tries a new row for the queen in that column.

# Q3: What are some optimizations that can be used in solving the N-Queens problem using CSP?
# A3: Some optimizations include:
# - **Forward checking**: Removing infeasible values from the domains of future variables.
# - **Constraint propagation**: Applying arc-consistency to reduce the domains during the search.

# Q4: What is **forward checking** in the context of the N-Queens problem?
# A4: Forward checking is used to eliminate any row values that are invalid (i.e., result in conflicts) in the future columns, 
# thus reducing the size of the search space.

# Q5: How can **constraint propagation** help solve the N-Queens problem efficiently?
# A5: Constraint propagation, such as enforcing arc-consistency, reduces the domains of variables early in the search process, 
# ensuring that only valid assignments are considered, thus speeding up the search.

# Q6: How does **Branch and Bound** apply to the N-Queens problem?
# A6: In **Branch and Bound**, the search tree is pruned by eliminating branches that cannot lead to a valid solution based on the 
# constraints. It uses bounds (e.g., the minimum number of queens left to place) to decide which branches to explore.
