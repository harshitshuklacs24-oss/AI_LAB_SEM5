
from collections import deque

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MAX_DEPTH = 30


# Generate possible moves
def get_neighbors(state):
    neighbors = []
    pos = state.index(0)

    row = pos // 3
    col = pos % 3

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)
            new_state[pos], new_state[new_pos] = (
                new_state[new_pos], new_state[pos]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# Display a puzzle state
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# 1. Breadth First Search
def bfs(start, goal, max_depth):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        depth = len(path) - 1

        if current == goal:
            return path

        if depth >= max_depth:
            continue

        for next_state in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


# 2. Depth First Search
def dfs(start, goal, max_depth):
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        depth = len(path) - 1

        if current == goal:
            return path

        if depth >= max_depth:
            continue

        for next_state in get_neighbors(current):
            if next_state not in path:
                stack.append((next_state, path + [next_state]))

    return None


# 3. Depth Limited Search (used by IDS)
def dls(state, goal, limit, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    for next_state in get_neighbors(state):
        if next_state not in path:
            result = dls(
                next_state, goal, limit - 1,
                path + [next_state]
            )

            if result is not None:
                return result

    return None


# 4. Iterative Deepening Search
def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, goal, depth, [start])

        if result is not None:
            return result

    return None


# Display algorithm results
def display_result(name, solution):
    print("\n" + name)

    if solution is None:
        print("No solution found within depth limit.")
        return

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)


# Main program
print("INITIAL STATE:")
print_board(start)

print("GOAL STATE:")
print_board(goal)

# Run all three algorithms
bfs_result = bfs(start, goal, MAX_DEPTH)
display_result("BFS", bfs_result)

dfs_result = dfs(start, goal, MAX_DEPTH)
display_result("DFS", dfs_result)

ids_result = ids(start, goal, MAX_DEPTH)
display_result("IDS", ids_result)
