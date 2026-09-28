
# 8-Puzzle using IDS

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


# Depth-limited DFS
def dls(state, goal, limit, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    for next_state in get_neighbors(state):
        if next_state not in path:
            result = dls(
                next_state,
                goal,
                limit - 1,
                path + [next_state]
            )

            if result is not None:
                return result

    return None


# Iterative Deepening Search
def ids(start, goal, max_depth=30):
    for depth in range(max_depth + 1):
        print("Searching at depth:", depth)

        result = dls(start, goal, depth, [start])

        if result is not None:
            return result

    return None


# Display solution
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


solution = ids(start, goal)

if solution:
    print("\nIDS Solution:")
    for state in solution:
        print_board(state)

    print("Number of moves:", len(solution) - 1)
else:
    print("No solution found within depth limit")

