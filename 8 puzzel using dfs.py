
# 8-Puzzle using DFS

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


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


# DFS algorithm
def dfs(start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        if current not in visited:
            visited.add(current)

            for next_state in get_neighbors(current):
                if next_state not in visited and next_state not in parent:
                    parent[next_state] = current
                    stack.append(next_state)

    return None


# Display solution
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


solution = dfs(start, goal)

if solution:
    print("DFS Solution:")
    for state in solution:
        print_board(state)

    print("Number of moves:", len(solution) - 1)
else:
    print("No solution found")
